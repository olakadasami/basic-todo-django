from django.shortcuts import render

# todos/views.py

from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'todos': todos, 'form': form}
    return render(request, 'todos/index.html', context)

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
