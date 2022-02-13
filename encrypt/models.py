from django.db import models

# Create your models here.

class EncryptText(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=64, null=False, blank=False)