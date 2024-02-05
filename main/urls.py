from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-retrieve-update-destroy'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrive-update-delete'),
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-retrive-update-delete'),
    path('devicelogs/', DeviceLogListCreateAPIView.as_view(), name='devicelog-list-create'),
    path('devicelogs/<int:pk>/', DeviceLogRetrieveUpdateDestroyAPIView.as_view(), name='devicelog-retrieve-update-destroy'),
]
