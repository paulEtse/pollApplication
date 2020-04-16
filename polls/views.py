from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello world, you are at the poll index. ")
def detail(request,question_id):
    return HttpResponse("You are looking at %s " %question_id)
def results(request,question_id):
    response = "You are looking for results of question %s " % question_id
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("You are voting question %s " % question_id)