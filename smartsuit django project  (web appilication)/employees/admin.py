from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("emp_id", "name", "dob", "gender", "mobile", "address",)


@admin.register(Suit)
class SuitAdmin(admin.ModelAdmin):
    list_display = ("suit_id", "full_name", )

