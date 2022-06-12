from django.shortcuts import render

from .models import Student, Xy
from .serializers import StudentSerializer, XySerializer, serializers
from rest_framework.generics import ListAPIView

from django.http import HttpResponse
import pandas as pd
import json

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class XyList(ListAPIView):
    queryset = Xy.objects.all()
    serializer_class = XySerializer

def func1(request):
    x_list = []
    y_list = []

    for i in range(1, 9):
        data = pd.read_excel("book3.xlsx", skiprows=i, usecols="A", nrows=0)
        # print (type(data.columns[0]))
        x_val = str(data.columns[0])
        data = pd.read_excel("book3.xlsx", skiprows=i, usecols="B", nrows=0)
        y_val = str(data.columns[0])
        # list1.append({'x': x_val, 'y': y_val})
        x_list.append(x_val)
        y_list.append(y_val)

        xy_data = Xy(x=x_val, y=y_val)  
        xy_data.save() 
    
    print("Type : ", type(x_list[0]))
    print("This is String : ", x_list[0])
    print("Type : ", type(int(x_list[0])))
    print('This is Integer : ', int(x_list[0]))
    print("Length of x_list:",len(x_list))
    print(x_list)
    print(y_list)

    xJson = json.dumps(x_list)
    yJson = json.dumps(y_list)

    print("Dumped file", xJson)
    print("Dumped file", yJson)
    return HttpResponse("Function is Working")