from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        if len(self.question_text) > 0:
            super().save(*args, **kwargs)

    @property
    def question(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text   = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.choice_text in ['a', 'b', 'c', 'd']:
            super().save(*args, **kwargs)
            print(f"You choose {self.choice_text}")

    @property
    def answer(self):
        return self.choice_text
