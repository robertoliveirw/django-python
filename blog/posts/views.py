from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworld(request):
    return HttpResponse('<h1>Hello World </h1> <br>I´m testing this method')

def secondview(request):
    return HttpResponse('Second View')

def post(request, id):
    return HttpResponse(id)
