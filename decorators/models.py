from django.db import models

# Create your models here.

class Loan(models.Model):
    user_name= models.CharField(max_length=200)
    amount = models.FloatField(null=True, default=0)
    number = models.CharField(max_length=10)

class Result(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.FloatField()

    class Meta:
        db_table = 'result'
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

Faculty_Choices = (
    ("TEACHING", "TEACHING"),
    ("NON-TEACHING", "NON-TEACHING"),
)
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=10)
    faculty_type = models.CharField(max_length=100, choices = Faculty_Choices)

    class Meta:
        db_table = 'faculty'
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
class AuthToken(models.Model):
    key = models.TextField()
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_token'
        verbose_name = 'Auth Token'
        verbose_name_plural = 'Auth Tokens'
