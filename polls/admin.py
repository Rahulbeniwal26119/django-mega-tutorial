from django.contrib import admin

from .models import Question, Choice


# from .models import
# Register your models here.


# StackedInline means one choice after another
# TabularInline means in table form
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # create custom field sets
    fieldsets = [
        ("Question Text", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]})
    ]
    # create choices with the question itself
    inlines = [ChoiceInline]
    # display individual columns
    # was_published_recently is a method
    list_display = ("question_text", "pub_date", "was_published_recently")
    # Specify either filed set or filed at once
    # fields = [f for f in Question().__dict__.keys() if f not in ["id", "_state"]]

    # Filter the objects according to pub_date
    list_filter = ["pub_date"]

    # filter according to question_text
    search_fields = ["question_text"]




admin.site.register(Question, QuestionAdmin)
# admin.site.register([Choice])
