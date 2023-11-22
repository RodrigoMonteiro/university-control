from django.db import models

class Professor(models.Model):

    nome = models.TextField()
    idade = models.IntegerField()
    

