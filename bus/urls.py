from django.contrib import admin
from django.urls import path, include
from .views import FromToList, FromToDetail

urlpatterns = [
    path('routes/', FromToList.as_view(), name='location-list'),
    path('routes/<int:pk>', FromToDetail.as_view(), name='location-detail'),
]