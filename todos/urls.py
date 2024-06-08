# todos/urls.py

from django.urls import path
from .views import index, delete_todo

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]
