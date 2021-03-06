from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

sources_router = SimpleRouter()
category_router = SimpleRouter()
incomes_router = SimpleRouter()
expenses_router = SimpleRouter()
set_date_router = SimpleRouter()
sources_router.register(r'sources', views.SourceViewSet, basename='sources')
category_router.register(r'categories', views.CategoryViewSet, basename='categories')
incomes_router.register(r'incomes', views.AllIncomesViewSet, basename='incomes')
expenses_router.register(r'expenses', views.AllExpensesViewSet, basename='expenses')
set_date_router.register(r'set-date', views.SetSalaryData, basename='set-date')


urlpatterns = [
    path('', views.index),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include(category_router.urls)),
    path('api/', include(sources_router.urls)),
    path('api/', include(incomes_router.urls)),
    path('api/', include(expenses_router.urls)),
    path('api/', include(set_date_router.urls)),
    # path('api/logout/', views.Logout.as_view()),
    # path('api/login/', views.Login.as_view()),
    path('api/relativity/', views.SetRelativity.as_view()),
    # path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # path('api/set-data/', views.SetSalaryData.as_view()),
    path('api/users/', views.UserAction.as_view()),
    # path('api/incomes/', views.AllIncomesViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('api/expenses/', views.AllExpensesViewSet.as_view({'get': 'list', 'post': 'create'})),
]
