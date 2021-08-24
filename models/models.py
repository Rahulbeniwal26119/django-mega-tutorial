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

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.place.name}"

# model field name cannot be a keyword
# field name cannot have more than single consequtive '_'
class Waiter(models.Model):
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} the waiter at {self.Restaurant}"

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"


# Custom Model Methods

class Human(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        import datetime
        if self.birth_date < datetime.date(195, 8, 1):
            return "Pre-Boomer"
        elif self.birth_date < datetime.date(1965,1,1):
            return "Baby Boomer"
        else:
            return "Post Boomer"

    @property
    def full_name(self):
        "returns the persons full name"
        return f"{self.first_name}  {self.last_name}"

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    def save(self, *args, **kwargs):
        if str( self.first_name) == 'Rahul':
            super().save(*args, **kwargs)  # class the actual save method
        else:
            print(" Unable to save")

    def delete(self, *args, **kwargs):
        print(" It will surely delete")
        super().delete(*args, **kwargs)
        print("SuccessFully Deleted")

# Model Inheritence
# abstract base class Inheritance

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        ordering = ['name']


# incase of multiple inheritence default for meta inheritance is the first class
class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False # django will not manage it like creating and modifying it

class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(Unmanaged.Meta):
        pass
        #db_table = 'student_info' # override the default scheme for naming tables

# related_name and realted_query_name
class Base(models.Model):
    m2m  =  models.ManyToManyField(
        CommonInfo,
        through="Medium",
        related_name="%(app_label)s_%(class)s_related",
        related_query_name = "%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True

class ChildA(Base):
    pass

class ChildB(Base):
    pass


class Medium(models.Model):
    common_info = models.ForeignKey(CommonInfo, on_delete=models.CASCADE)
    childA = models.ForeignKey(ChildA, on_delete=models.CASCADE)
    childB = models.ForeignKey(ChildB, on_delete=models.CASCADE)

# Multi Table Inheritance
class Places(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurants(Places):
    servers_hot_dogs = models.BooleanField(default=False)
    servers_pizza = models.BooleanField(default=True)

class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='provider')

# proxy model inheritance
# unmanaged vs proxy
# important but lagging is how to create customer Manager
class NewManager(models.Manager):
    pass

class ProxyPerson(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class ProxyMyPerson(ProxyPerson):
    objects = NewManager()
    class Meta:
        ordering = ["last_name"]
        proxy = True

    def do_something(self):
        pass

# Multiple Inheritance
# use different primary key to abstain from conflict
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)

class BookArticle(Book, Article):
    pass

# Alternate way to abstain from conflict make
# use a common ancestor to hold the AutoField
# hiding is only allowed in inheritance from Abstract Class
class Piece(models.Model):
    pass

class Article2(Piece):
    article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)

class Book2(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)

class BookReview(Article2, Book2):
    pass

class Reporter(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class NewsArticle(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    content = models.TextField()

