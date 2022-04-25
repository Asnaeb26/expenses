from django.shortcuts import render
from .models import *
from . import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import Response, APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework import mixins


def index(request):
    return render(request, 'app_expenses/index.html')


class SourceViewSet(ModelViewSet):
    """Список всех категорий пользователя"""
    queryset = IncomeCategory.objects.all()
    serializer_class = serializers.SourceSerializer
    lookup_field = 'id'


class AllIncomesViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer


class CategoryViewSet(ModelViewSet):
    """Список категорий затрат"""
    queryset = ExpenseCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'pk'


class AllExpensesViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer

    def create(self, request, *args, **kwargs):
        data_list = request.data.get('data')
        serializer = serializers.ExpenseSerializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class SetSalaryDay(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = serializers.ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        income_id = request.data.get('source')
        salary_day = request.data.get('salary_day')
        obj, _ = Client.objects.update_or_create(
            source_id=income_id,
            defaults={'salary_day': salary_day},
        )
        serializer = serializers.ClientSerializer(obj)
        return Response(serializer.data, status=HTTP_200_OK)


class SetRelativity(APIView):
    def get(self, request):
        serializer = serializers.RelativitySerializer(Relativity.objects.first())
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get('name')
        value = request.data.get('value')
        amount = request.data.get('amount')
        if Relativity.objects.count() != 0:
            Relativity.objects.update(name=name, value=value, amount=amount)
        else:
            Relativity.objects.create(name=name, value=value, amount=amount)
        relativity = Relativity.objects.first()
        serializer = serializers.RelativitySerializer(relativity)
        return Response(serializer.data, status=HTTP_200_OK)
