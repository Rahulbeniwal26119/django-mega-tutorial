# from django.shortcuts import render
# from django.template import loader
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import simplejson as json
# from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from rest_framework.decorators import api_view 
from rest_framework import status
from .models import Question, Choice
from shared.request_utils import log_and_respond


# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     output = '<br>'.join([f"Q. {q.question_text}" for q in latest_question_list])
#     template = loader.get_template('polls/index.html')
#     context = {
#             "latest_question_list" : latest_question_list
#     }
#     return render(request, 'polls/index.html', context)
# return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects. \
                   filter(pub_date__lte=timezone.now()) \
                   .order_by("-pub_date")[:5]


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {'question' : question})
# return HttpResponse(f"You are looking at the question {question_id}")

# def detail2(request, question_id):
# #     # question_list = get_list_or_404(Question) like using filter instead of get
# #     question = get_object_or_404(Question, pk=question_id)
# #     context = {
# #         'question' : question
# #     }
# #     return render(request, "polls/detail.html", context)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """Excludes the question which are not published yet"""
        return Question.objects.filter(pub_date__lte=timezone.now())


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
# return render(request, "polls/results.html", {'question' : question})

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        print(selected_choice.choice_text)
        print(selected_choice.votes)
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@api_view(['GET'])
def custom_view(request):

    print("get -> ", request.GET)
    print("data -> ", request.data)
    params = request.GET.get('params')
    print(params)
    return log_and_respond(
        data = {"message": "Hello World"},
        status = status.HTTP_200_OK,
        message="succeefully done",
        message_code = "200"
    )