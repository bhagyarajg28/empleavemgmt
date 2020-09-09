from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Employee(models.Model):
    employee_name=models.ForeignKey(User, on_delete=models.CASCADE)
    start_date=models.DateField(blank=False)
    end_date=models.DateField(blank=False)
    description=models.CharField(max_length=50,blank=False)
    total_leaves=models.PositiveSmallIntegerField(default=15)
    leave_status=models.BooleanField(default=False)




class Manager(models.Model):
    manager_name=models.ForeignKey(User, on_delete=models.CASCADE)
    emp_name=models.ForeignKey(Employee,on_delete=models.CASCADE)




