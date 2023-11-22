from django.db import models
from professor.models import Professor
from curso.models import Curso

class Disciplina(models.Model):

    nome = models.TextField()
    carga_horaria = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso,  on_delete=models.PROTECT)
