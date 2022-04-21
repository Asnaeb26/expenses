from rest_framework import serializers
from . import models


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'