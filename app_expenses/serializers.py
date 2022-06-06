from rest_framework import serializers

from .models import *


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
        extra_kwargs = {'category': {'write_only': True}}
        # exclude = ('category',)

    def create(self, validated_data):
        # validated_data['category_id'] = self.initial_data.get('category_id')
        return Income.objects.create(**validated_data)


class SourceSerializer(serializers.ModelSerializer):
    data = IncomeSerializer(source='income', many=True, read_only=True)

    class Meta:
        model = IncomeCategory
        fields = ('id', 'name', 'color', 'data',)

    def create(self, validated_data):
        user_id = self.initial_data.get('user_id')
        validated_data['user_id'] = user_id
        return IncomeCategory.objects.create(**validated_data)


# ______________________________________________________________________
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        extra_kwargs = {'category': {'write_only': True}}

    def create(self, validated_data):
        return Expense.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    data = ExpenseSerializer(source='expenses', many=True, read_only=True)

    class Meta:
        model = ExpenseCategory
        fields = ('name', 'nameRusCase', 'color', 'data')

    def create(self, validated_data):
        user_id = self.initial_data.get('user_id')
        validated_data['user_id'] = user_id
        return ExpenseCategory.objects.create(**validated_data)


# ________________________________________________________________________
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        # fields = '__all__'
        exclude = ('id', 'user')

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.salary_day = validated_data.get('salary_day', instance.salary_day)
        instance.salary_month = validated_data.get('salary_month', instance.salary_month)
        instance.source = validated_data.get('source', instance.source)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class RelativityCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelativeCase
        exclude = ('id', 'relativity',)


class RelativitySerializer(serializers.ModelSerializer):
    case = RelativityCaseSerializer()

    class Meta:
        model = Relativity
        fields = ('id', 'name', 'value', 'amount', 'case',)

    def create(self, validated_data):
        cases_date = validated_data.pop('case')
        user = self.initial_data.get('user_instance')
        validated_data['user'] = user
        name = validated_data.get('name')
        current_rel = Relativity.objects.filter(user_id=user.id)
        if current_rel.count() != 0:
            current_rel.update(**validated_data)
            relativity = current_rel.get(name=name)
            RelativeCase.objects.filter(relativity=relativity).update(**cases_date)
        else:
            relativity = Relativity.objects.create(**validated_data)
            RelativeCase.objects.create(relativity=relativity, **cases_date)
        return relativity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
