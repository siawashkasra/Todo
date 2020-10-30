from django.shortcuts import render
from django.shortcuts import render
from .models import Todo


# Create your views here.

todos = Todo.objects.all()

def index(request):
    return render(request, 'todos/index.html', {'todos': todos})
    