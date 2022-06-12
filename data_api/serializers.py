from sys import stdlib_module_names
from rest_framework import serializers
from .models import Student, Xy

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name', 'email', 'phone']
        
class XySerializer(serializers.ModelSerializer):
    class Meta:
        model = Xy
        fields = ['x', 'y']