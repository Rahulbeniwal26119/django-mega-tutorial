from django.contrib import admin
from .models import Question, Choice
# from .models import
# Register your models here.
admin.site.register([Question, Choice])
