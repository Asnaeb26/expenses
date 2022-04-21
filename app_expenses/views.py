from django.shortcuts import render
from .models import Expense, Income, Relativity, Category
from . import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet


def index(request):
    return render(request, 'app_expenses/index.html')


class CategoryViewSet(ModelViewSet):
    """Список всех категорий пользователя"""
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ExpenseViewSet(ModelViewSet):
    """Список всех затрат пользователя"""
    queryset = Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


class IncomeViewSet(ModelViewSet):
    """Список всех доходов пользователя"""
    queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer

