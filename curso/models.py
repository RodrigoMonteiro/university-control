from django.db import models

class Curso(models.Model):

    nome = models.TextField()
    semestres = models.IntegerField()
    numero_disciplinas = models.IntegerField()
    carga_horaria = models.IntegerField()
