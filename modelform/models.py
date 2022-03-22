from django.db import models

class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=40)
    phone_number  = models.CharField(max_length=10)

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="course")

    def __str__(self):
        return self.name