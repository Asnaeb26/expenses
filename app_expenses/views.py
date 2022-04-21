from django.shortcuts import render
from .models import Expense, Income, Relativity, Category
from .serializers import ExpenseSerializer, IncomeSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet


def index(request):
    return render(request, 'app_expenses/index.html')


class CategoryViewSet(ModelViewSet):
    """Список всех категорий пользователя"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(ModelViewSet):
    """Список всех затрат пользователя"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class IncomeViewSet(ModelViewSet):
    """Список всех доходов пользователя"""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
