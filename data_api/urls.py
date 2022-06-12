from django.urls import path
from data_api import views

urlpatterns = [
    path('student/',views.StudentList.as_view()),
    path('xy/',views.XyList.as_view()),
    path('func1/',views.func1),
]