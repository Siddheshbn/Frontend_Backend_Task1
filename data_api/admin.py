from django.contrib import admin
from .models import Student, Xy

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'email', 'phone']

@admin.register(Xy)
class XyAdmin(admin.ModelAdmin):
    list_display = ['x', 'y']
