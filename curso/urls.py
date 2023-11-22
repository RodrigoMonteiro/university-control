from django.urls import path
from .views import create_curso, delete_curso, update_curso, get_all_cursos

urlpatterns = [
    path('', get_all_cursos, name="get-all-cursos" ),
    path('create', create_curso, name="create-curso" ),
    path('update/<int:id>', update_curso, name="update-curso" ),
    path('delete/<int:id>', delete_curso, name="delete-curso" ),
]
