from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter


sources_router = SimpleRouter()
category_router = SimpleRouter()
sources_router.register(r'sources', views.SourceViewSet, basename='sources')
category_router.register(r'categories', views.CategoryViewSet, basename='categories')


urlpatterns = [
    path('', views.index),
    path('api/', include(category_router.urls)),
    path('api/', include(sources_router.urls)),
    path('api/relativity/', views.SetRelativity.as_view()),
    path('api/set-data/', views.SetSalaryData.as_view()),
    path('api/incomes/', views.AllIncomesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/expenses/', views.AllExpensesViewSet.as_view({'get': 'list', 'post': 'create'})),
]
