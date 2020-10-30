from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Todo
import datetime

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})
    
def create(request):
    if request.POST:
        todo = Todo(
            title=request.POST.get('title'), 
            description=request.POST.get('description'),
            priority=request.POST.get('priority')
            )
        todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = Todo.objects.filter(id=todo_id)
    todo.delete()
    return redirect('index')

def complete(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).first()
    todo.is_completed = True
    todo.completed_at = datetime.datetime.now()
    todo.save()
    return redirect('index')