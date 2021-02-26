from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a test response page")

def detail(request, question_id):
    return HttpResponse('This is a page of question %s.' % question_id)

def result(request, question_id):
    response = 'These are results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)