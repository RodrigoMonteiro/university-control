from django.urls import path
from .views import create_disciplina, delete_disciplina, get_all_disciplinas, update_disciplina
urlpatterns = [

    path('', get_all_disciplinas, name='get-all-disciplinas'),
    path('create', create_disciplina , name='create-disciplina'),
    path('update/<int:id>', update_disciplina, name='update-disciplina'),
    path('delete/<int:id>', delete_disciplina, name='delete-disciplina'),
]
