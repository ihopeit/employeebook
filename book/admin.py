from django.contrib import admin

# Register your models here.

from book.models import Employee

admin.site.register(Employee)