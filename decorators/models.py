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

# Prefetch related and selected related 
class Province(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name 


class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name 


class Persons(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hometown = models.ForeignKey(City, on_delete=models.CASCADE, related_name="birth")
    visitation = models.ManyToManyField(City, related_name="visitors")
    living = models.ForeignKey(City, on_delete=models.CASCADE,  related_name="citizen")

    def __unicode__(self):
        return self.first_name + " " + self.last_name