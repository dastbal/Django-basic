from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.


def index(request):
    questions = Question.objects.all()
    return render(request, "polls/index.html", {
        "questions": questions
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/results.html", {
        "question": question
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        vote = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "errorMsg": "No elegiste una repuesta"
        })
    else:
        vote.votes += 1
        vote.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
