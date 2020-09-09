from django.contrib import admin
from .models import Employee, Manager


# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    pass


class Managerdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, Employeeadmin)
admin.site.register(Manager, Managerdmin)
