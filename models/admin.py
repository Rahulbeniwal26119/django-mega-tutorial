from django.contrib import admin
from .models import Car, Musician, Manufacturer, Person, Album, WorkShop
# Register your models here.

admin.site.register([Car, Musician, Manufacturer, Person, Album, WorkShop])