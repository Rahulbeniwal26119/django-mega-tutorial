from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        # what the hack is this swappable here
        # it fixed the error with user change
        db_table = 'customuser_customuser'

class TestUser(models.Model):
    name = models.TextField()
