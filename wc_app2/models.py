from django.db import models

# Create your models here.
class Student(models.Model):
    s_name=models.CharField(max_length=16)
    s_age=models.IntegerField(default=1)

class grade(models.Model):
    grade_name=models.CharField(max_length=16,default="未命名班级")


