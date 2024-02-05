from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'user']


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['user']

        
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Employee
        fields = ['user', 'company',]


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['user', 'company',]

class DeviceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Device
        fields = '__all__'
        
class DeviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceLogSerializer(serializers.ModelSerializer):
    # device = DeviceSerializer(read_only=True)
    # employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = DeviceLog
        fields = '__all__'
        # fields = ['id', 'device', 'employee', 'check_in_date', 'check_out_date', 'condition_when_checked_out', 'condition_when_checked_in', 'description']


