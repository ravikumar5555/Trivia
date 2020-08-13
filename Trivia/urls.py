from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('first', views.first_question, name='first_question'),
    path('second', views.second_question, name='second_question'),
    path('summary', views.summary, name='summary'),
    path('history', views.history, name='history'),
]