from django.shortcuts import render
from .models import Expense, Income, Relativity, IncomeCategory
from . import serializers
from . import logic
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


def index(request):
    return render(request, 'app_expenses/index.html')


class SourceViewSet(ModelViewSet):
    """Список всех категорий пользователя"""
    queryset = IncomeCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'id'


class ExpenseViewSet(ModelViewSet):
    """Список всех затрат пользователя"""
    queryset = Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


class IncomeViewSet(ModelViewSet):
    """Список всех доходов пользователя"""
    queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Income.objects.filter(category_id=self.kwargs.get('id'))

    def create(self, request, *args, **kwargs):
        income = logic.MoneyAction(request.data, kwargs.get('id'))
        data = income.create_data()
        serializer = serializers.IncomeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
