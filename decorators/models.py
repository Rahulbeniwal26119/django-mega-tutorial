from django.db import models

# Create your models here.

class Loan(models.Model):
    user_name= models.CharField(max_length=200)
    amount = models.FloatField(null=True, default=0)
    number = models.CharField(max_length=10)

