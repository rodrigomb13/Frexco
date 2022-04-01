from django.urls import path

from .views import RegionsAPIView,RegionAPIView, FruitsAPIView, FruitAPIView

urlpatterns = [
    path('regions/', RegionsAPIView.as_view(), name='regions'),
    path('fruits/', FruitsAPIView.as_view(), name='fruits'),
    path('regions/<int:pk>/', RegionAPIView.as_view(), name='region'),
    path('fruits/<int:pk>/', FruitAPIView.as_view(), name='fruit'),
]