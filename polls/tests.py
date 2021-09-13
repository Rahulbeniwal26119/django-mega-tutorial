import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


# Create your tests here.


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past Question", days=-30)
        create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past Question 1", days=-30)
        question2 = create_question(question_text="Past Question 2", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question2, question1])


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past Question", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

