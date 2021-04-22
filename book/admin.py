from django.contrib import admin

# Register your models here.

from book.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    ## 编辑页不展示字段列表
    exclude = ('created_date','updated_date')

    list_display = ('empno', 'name', 'email', 'mobile', 'status', 'dept1', 'created_date', 'updated_date')

    list_filter = ('dept1','status','office_city','edu_school')

    search_fields = ('empno','name','email','mobile', 'dept1',)

admin.site.register(Employee, EmployeeAdmin)
