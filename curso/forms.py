from django import forms
from curso.models import Curso


class CursoForm(forms.ModelForm):
    
    class Meta:
        model = Curso
        fields = ['nome','semestres','numero_disciplinas' ,'carga_horaria']
