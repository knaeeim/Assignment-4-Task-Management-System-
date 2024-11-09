from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_task/', add_task, name="add_task"),
    path('edit_task/<int:id>', edit_task, name="edit_task"),
    path('delete_task/<int:id>', delete_task, name="delete_task")
]