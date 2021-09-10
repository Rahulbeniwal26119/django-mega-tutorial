from django.db import models

class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=40)
    phone_number  = models.CharField(max_length=10)
# Create your models here.
