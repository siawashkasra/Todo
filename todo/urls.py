from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('complete/<int:todo_id>', views.complete, name='complete')
]

