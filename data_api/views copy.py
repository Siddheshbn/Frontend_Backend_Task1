from django.shortcuts import render

from .models import Student, Xy
from .serializers import StudentSerializer, XySerializer, serializers
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class XyList(ListAPIView):
    queryset = Xy.objects.all()
    serializer_class = XySerializer