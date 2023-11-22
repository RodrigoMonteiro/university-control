from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from professor.forms import ProfessorForm

from professor.models import Professor

def create_professor(request):
    if request.method =='POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('get-all-professores'))
    else:
            form = ProfessorForm()

    return render(request, 'professor/createProfessor.html', {'forms': form})

def get_all_professores(request):
    all_professores = Professor.objects.all()
    return render (request, 'professor/getAllProfessores.html', {'professores': all_professores})

def update_professor(request, id):
    selected_professor = Professor.objects.get(id = id)
    if request.method == 'POST':
        selected_professor.nome = request.POST.get('nome')
        selected_professor.idade = request.POST.get('idade')
        selected_professor.save()
        return redirect(reverse_lazy('get-all-professores'))

    return render (request,'professor/updateProfessor.html', {'professor':selected_professor})

def delete_professor(request, id):
      selected_professor = Professor.objects.get(id = id)
      if request.method == 'POST':
          selected_professor.delete()
          return redirect(reverse_lazy('get-all-professores')) 
      return render (request,'professor/deleteProfessor.html', {'professor':selected_professor})

