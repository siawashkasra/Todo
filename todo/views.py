from django.shortcuts import render
from django.shortcuts import render
from .models import Todo
from django.http import HttpResponse


# Create your views here.

todos = Todo.objects.all()

def index(request):
    return render(request, 'todos/index.html', {'todos': todos})
    
def create(request):
    print(request)
    return HttpResponse('This is create!')