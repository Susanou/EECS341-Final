from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World! You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question # %s" %question_id)

def result(request, question_id):
    return HttpResponse("you're looking at the result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting for question %s" % question_id)