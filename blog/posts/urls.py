from django.urls import path
from . import views

urlpattern = [
    path('helloworld/', views.helloworld)
]