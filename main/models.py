from django.contrib.auth.models import User
from django.db import models

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
         return f'{self.name}'

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
         return f'Company:{self.company} User:{self.user}'


CONDITION_CHOICES = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    current_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    
    def __str__(self):
         return f'Company:{self.company} Name:{self.name}'


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(null=True, blank=True)
    check_out_date = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good')
    condition_when_checked_in = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good')
    
    description = models.CharField( max_length=200,null=True, blank=True)
    
    
    def __str__(self):
         return f'Device:{self.device.name} Employee:{self.employee.user}'


