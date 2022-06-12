from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)

class Xy(models.Model):
    x = models.DecimalField(max_digits=15, decimal_places=9)
    y = models.DecimalField(max_digits=15, decimal_places=9)

