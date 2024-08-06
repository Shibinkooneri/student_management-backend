from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    Number=models.IntegerField(unique=True)
    age=models.IntegerField()
    Enrollment_Date=models.DateField()
    course=models.CharField(max_length=100)