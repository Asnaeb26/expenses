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


class SetSalaryData(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = serializers.ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = serializers.ClientSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def put(self, request):
        data = request.data
        instance = Client.objects.get(source_id=data.get('source'))
        serializer = serializers.ClientSerializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class SetRelativity(APIView):
    def get(self, request):
        serializer = serializers.RelativitySerializer(Relativity.objects.first())
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = serializers.RelativitySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)

    # {
    #     "name": "Пиво",
    #     "value": "л",
    #     "amount": 5.0,
    #     "case": {
    #         "name1": "Пива",
    #         "name2": "Пив",
    #         "name3": "Пиво"
    #     }
    #
    # }
