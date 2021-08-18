from django.db import models
from django.utils.translation import LANGUAGE_SESSION_KEY

# Create your models here.

class Person(models.Model):
    SHIRT_SIZES  = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    # first is use as value
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    Genre = models.TextChoices( 'Classical', 'Jazz') # another way to use choices limited to maximum two elements
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField(blank=True) # now this is a optional field
    genre_type = models.CharField(max_length=10, blank=True, choices=Genre.choices)

class WorkShop(models.Model):
    event_name = models.CharField(max_length=100, default="Workshop", unique=True)
    event_id = models.BigAutoField(blank=False, primary_key=True)   # if not specified then automatically a field will created
