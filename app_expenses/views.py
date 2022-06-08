from django.shortcuts import render
from .models import *
from . import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import Response, APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework import permissions
from app_expenses import logic
from rest_framework import mixins
from rest_framework_simplejwt.tokens import RefreshToken


def index(request):
    return render(request, 'app_expenses/index.html')


# class Logout(APIView):
#     def post(self, request):
#         token = RefreshToken(request.auth)
#         token.blacklist()
#         return Response({"message": "юзер не залогинен"}, status=HTTP_200_OK)
#
#
# class Login(APIView):
#     permission_classes = (permissions.AllowAny, )
#
#     def post(self, request):
#         username = request.data.get('username')
#         token = request.auth
#         user = User.objects.get(username=username)
#         if user:
#             token.check_blacklist()
#             return Response({"OK": "OKOKOKOKOKOKO"})
#         else:
#             return Response({"sss": "fdfdfdf"})


class SourceViewSet(ModelViewSet):
    """Список всех категорий пользователя"""
    # queryset = IncomeCategory.objects.all()
    serializer_class = serializers.SourceSerializer
    lookup_field = 'id'

    # permission_classes = permissions.IsAuthenticated

    def get_queryset(self):
        return IncomeCategory.objects.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        category = request.data
        category['user_id'] = request.user.id
        serializer = serializers.SourceSerializer(data=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


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
    # queryset = ExpenseCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return ExpenseCategory.objects.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        category = request.data
        category['user_id'] = request.user.id
        serializer = serializers.CategorySerializer(data=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


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


# class SetSalaryData(APIView):
class SetSalaryData(ModelViewSet):
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return Client.objects.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = serializers.ClientSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        ins = Client.objects.get(pk=kwargs['pk'])
        serializer = serializers.ClientSerializer(instance=ins, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class SetRelativity(APIView):
    def get(self, request):
        relativity = Relativity.objects.get(user_id=request.user)
        serializer = serializers.RelativitySerializer(relativity)
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
        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)
