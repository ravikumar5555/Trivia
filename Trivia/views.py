from django.http import HttpResponse
from django.shortcuts import render
from .models import Game


def index(request):
    return render(request, 'Trivia/index.html')


def first_question(request):
    request.session['username'] = request.POST.get('username')
    question = 'Who is the best cricketer in the world?'
    request.session['question1'] = question
    options = ['Sachin Tendulkar', 'Virat Kolli', 'Adam Gilchirst', 'Jacques Kallis']
    context = { 'question' : question, 'options' : options}
    return render(request, 'Trivia/first.html', context)


def second_question(request):
    request.session['choice1'] = request.POST.get('choice')
    question = 'What are the colors in the Indian national flag? Select all'
    options = ['White', 'Yellow', 'Orange', 'Green']
    request.session['question2'] = question
    context = {'question': question, 'options': options}
    return render(request, 'Trivia/second.html', context)


def summary(request):
    request.session['choice2'] = request.POST.getlist('choice')
    context = {
        'username': request.session.get('username'),
        'question1': request.session.get('question1'),
        'choice1': request.session.get('choice1'),
        'question2': request.session.get('question2'),
        'choice2': ', '.join(request.session.get('choice2')),
    }

    game = Game(**context)
    game.save()
    request.session.flush()
    return render(request, 'Trivia/summary.html', context)


def history(request):
    games = Game.objects.all()
    return render(request, 'Trivia/history.html', {'games':games})