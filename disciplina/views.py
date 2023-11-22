from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from curso.models import Curso

from disciplina.forms import DisciplinaForm
from disciplina.models import Disciplina
from professor.models import Professor


def create_disciplina(request):
    all_cursos = Curso.objects.all()
    all_professores = Professor.objects.all()

    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('get-all-disciplinas'))
    else:
        form = DisciplinaForm()
    return render(request, 'disciplina/createDisciplina.html', {'forms': form, 'cursos':all_cursos, 'professores': all_professores})

def get_all_disciplinas(request):
    all_disciplinas = Disciplina.objects.all()
    return render(request, 'disciplina/getAllDisciplinas.html', { 'disciplinas':all_disciplinas})

def update_disciplina(request,id):
    all_cursos = Curso.objects.all()
    all_professores = Professor.objects.all()
    selected_disciplina = Disciplina.objects.get(id=id)
    if request.method == 'POST':
        selected_disciplina.nome = request.POST.get('nome')
        selected_disciplina.carga_horaria = request.POST.get('carga_horaria')
        selected_disciplina.professor = Professor.objects.get(id= request.POST.get('professor'))
        selected_disciplina.curso= Curso.objects.get(id= request.POST.get('curso'))
        selected_disciplina.save()
        return redirect(reverse_lazy('get-all-disciplinas'))

    return render (request, 'disciplina/updateDisciplina.html', { 'disciplina':selected_disciplina, 'cursos':all_cursos,'professores' :all_professores})

def delete_disciplina(request,id):
    selected_disciplina = Disciplina.objects.get(id=id)
    if request.method == 'POST':
        selected_disciplina.delete()
        return redirect(reverse_lazy('get-all-disciplinas'))
    return render (request, 'disciplina/deleteDisciplina.html', { 'disciplina':selected_disciplina})
