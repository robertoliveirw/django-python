from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World<br>I´m testing this method')

def secondview(request ):
    return HttpResponse('Second View')