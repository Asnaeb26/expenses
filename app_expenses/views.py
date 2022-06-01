import json

from django.shortcuts import render
from .models import *
from . import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import Response, APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework import permissions
from app_expenses import logic
from rest_framework import mixins
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'app_expenses/index.html')


class SourceViewSet(ModelViewSet):
    """Список всех категорий пользователя"""
    queryset = IncomeCategory.objects.all()
    serializer_class = serializers.SourceSerializer
    lookup_field = 'id'
    permission_classes = permissions.IsAuthenticated


# class AllIncomesViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
class AllIncomesViewSet(ModelViewSet):
    # queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer

    def get_queryset(self):
        return Income.objects.filter(user_id=self.request.user.id)
        # return Income.objects.filter(user_id=self.request.user).values_list('user_id', flat=True)

    def create(self, request, *args, **kwargs):
        serializer = serializers.IncomeSerializer(data=logic.get_income(request.data, request.user))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class CategoryViewSet(ModelViewSet):
    """Список категорий затрат"""
    queryset = ExpenseCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'pk'


# class AllExpensesViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
class AllExpensesViewSet(ModelViewSet):
    # queryset = Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        data_list = logic.get_expenses(request.data.get('data'), request.user)
        serializer = serializers.ExpenseSerializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class SetSalaryData(APIView):
    def get(self, request):
        queryset = Client.objects.filter(user_id=self.request.user.id)
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
        serializer = serializers.RelativitySerializer(Relativity.objects.get(user_id=request.user))
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['user_instance'] = request.user
        serializer = serializers.RelativitySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


class UserAction(APIView):
    def get(self, request):
        serializer = serializers.UserSerializer()
        return Response(serializer.data)
