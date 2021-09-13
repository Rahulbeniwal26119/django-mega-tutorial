from django.contrib import admin

from .models import Question, Choice


# from .models import
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    # create custom field sets
    fieldsets = [
        ("Question Text", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]})
    ]
    # fields = [f for f in Question().__dict__.keys() if f not in ["id", "_state"]]


admin.site.register(Question, QuestionAdmin)
admin.site.register([Choice])
