from rest_framework import serializers

from . import models


class IncomeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Income
        fields = '__all__'

    def create(self, validated_data):
        validated_data['category_id'] = self.initial_data.get('category_id')
        return models.Income.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    income = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.IncomeCategory
        fields = '__all__'
        depth = 1


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'
