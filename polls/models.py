from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        if len(self.question_text) > 0:
            super().save(*args, **kwargs)

    # # order the item according pub_date
    # @admin.display(
    #     boolean = True,
    #     ordering = "pub_date",
    #     description = "Published Recently?"
    # )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_not_valid(self):
        return self.question_text == ''

    @property
    def question(self):

        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text   = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        #if self.choice_text in ['a', 'b', 'c', 'd']:
        super().save(*args, **kwargs)
        #print(f"You choose {self.choice_text}")

    @property
    def answer(self):
        return self.choice_text

    def __str__(self):
        return self.choice_text


class Marks(models.Model):
    name = models.CharField(max_length=200)
    english = models.IntegerField()
    maths = models.FloatField()
    science = models.FloatField()

    class Meta:
        db_table = "marks"
        verbose_name = "Marks"

# annotate in django 
# In [18]: Marks.objects.all().values('name').distinct('name').annotate(total_marks=F('en
    #    1 glish') + F('maths')+ F('science'))
# Out[18]: <QuerySet [{'name': 'Kuldeep', 'total_marks': 160.0}, {'name': 'Rahul', 'total_marks': 300.0}]>
# aggregate in django
# In [22]: Marks.objects.all().values('name').aggregate(Sum('english')).get('english__sum
    #    1 ')
# Out[22]: 123
# annotate applies on a tuple
# aggregate applies on a single value or cols