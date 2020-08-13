from django.db import models

# Create your models here.


class Game(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=50)
    question1 = models.CharField(max_length=500)
    choice1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=100)
