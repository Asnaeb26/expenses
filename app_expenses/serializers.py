from rest_framework import serializers

from .models import *


class IncomeSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(read_only=True)
    # category = serializers.IntegerField(write_only=True)
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
        fields = ('id', 'name', 'color', 'data')


# ________________________________________________________________________
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class RelativitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relativity
        fields = '__all__'
