from django.db import models

class Game(models.Model):
    gameName = models.CharField(max_length=100)
    gameInfo = models.CharField(max_length=100)
