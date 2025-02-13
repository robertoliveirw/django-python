from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('home/', views.home),
    path('<int:id>/', views.post), 
]