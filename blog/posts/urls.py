from django.urls import path
from . import views

urlpattern = [
    path('post/helloworld/', views.helloworld)
]