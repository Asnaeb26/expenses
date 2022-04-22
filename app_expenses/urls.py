from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

expenses_router = SimpleRouter()
incomes_router = SimpleRouter()
categories_router = SimpleRouter()
expenses_router.register(r'expenses', views.ExpenseViewSet, basename='expenses')
incomes_router.register(r'incomes', views.IncomeViewSet, basename='incomes')
categories_router.register(r'sources', views.SourceViewSet, basename='sources')


urlpatterns = [
    path('', views.index),
    path('api/', include(expenses_router.urls)),
    path('api/', include(categories_router.urls)),
    path('api/sources/<int:id>/', include(incomes_router.urls)),
]
