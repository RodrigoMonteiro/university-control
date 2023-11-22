from django.urls import path
from .views import create_professor, delete_professor,update_professor, get_all_professores

urlpatterns = [
    path('', get_all_professores,name='get-all-professores'),
    path('create',create_professor,name='create-professor'),
    path('update/<int:id>',update_professor,name='update-professor'),
    path('delete/<int:id>',delete_professor,name='delete-professor')
]
