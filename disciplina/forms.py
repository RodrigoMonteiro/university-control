from django import forms
from disciplina.models import Disciplina


class DisciplinaForm(forms.ModelForm):
    
    class Meta:
        model = Disciplina
        fields = ['nome','carga_horaria','professor','curso']
