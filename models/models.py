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

    def __str__(self):
        return self.first_name + self.last_name

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    Genre = models.TextChoices( 'Classical', 'Jazz') # another way to use choices limited to maximum two elements
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name="Artist")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField(blank=True) # now this is a optional field
    genre_type = models.CharField(max_length=10, blank=True, choices=Genre.choices)

class WorkShop(models.Model):
    event_name = models.CharField("Event Name", max_length=100, default="Workshop", unique=True)
    event_id = models.BigAutoField(blank=False, primary_key=True)   # if not specified then automatically a field will created

class Manufacturer(models.Model):
    name = models.CharField("Manufacturer Name", max_length=30, default="Toyota",
    blank=True, primary_key=True)

    def __str__(self):
        return self.name

# Foreign Key is used to setup many to one relation ship 
class Car(models.Model):
    name = models.CharField(max_length=100, default="Xeon")
    Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Manuacturer name")

# Many to Many
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name

class MemberShip(models.Model):
    person   = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


# One to One Relation 

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.address} the place"

class Restaurtant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    servers_hot_dogs = models.BooleanField(default=False)
    servers_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.place.name}"

class Waiter(models.Model):
    restaurtant = models.ForeignKey(Restaurtant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} the waiter at {self.restaurtant}"


