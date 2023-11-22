from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from curso.forms import CursoForm
from curso.models import Curso

def create_curso(request):
    if request.method == 'POST':
     form = CursoForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect(reverse_lazy('get-all-cursos'))
    else:
     form = CursoForm()
    return render(request, 'curso/createCurso.html', {'forms': form})

def get_all_cursos(request):
   all_cursos = Curso.objects.all()
   return render(request, 'curso/getAllCursos.html', {'cursos': all_cursos})

def update_curso(request,id):
    selected_curso =  Curso.objects.get(id=id)
    if request.method == 'POST':
     selected_curso.nome = request.POST.get('nome')
     selected_curso.semestres = request.POST.get('semestres')
     selected_curso.numero_disciplinas = request.POST.get('numero_disciplinas')
     selected_curso.carga_horaria = request.POST.get('carga_horaria')
     selected_curso.save()
     return redirect(reverse_lazy('get-all-cursos'))
    return render(request, 'curso/updateCurso.html', {'curso': selected_curso})
    

def delete_curso(request,id):
       selected_curso =  Curso.objects.get(id=id)
       if request.method == 'POST':
        selected_curso.delete()
        return redirect(reverse_lazy('get-all-cursos'))
       return render(request, 'curso/deleteCurso.html', {'curso': selected_curso})
