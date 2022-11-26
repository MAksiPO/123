from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import TodoItem
from .models import *
from .forms import TodoForm
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView,
)
from django.views import View
from .forms import UserRegForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegForm()
    context = {
        'form': form
    }
    return render(request, 'todo_app/register/Regestration_front.html', context=context)

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'todo_app/log/login.html', context=context)

def logout_user(request):
    logout(request)
    return redirect('login')

def home_page(request):
    return render(request, 'todo_app/home_page/index.html', context={register: "register"})

def Todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = TodoItem.objects.all()
            return render(request, 'todo_app/todo_main/home.html', {'todos': todos, 'form' : form})
    else:
        todos = TodoItem.objects.all()
        return render(request, 'todo_app/todo_main/home.html', {'todos': todos})

def delete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, ('Task has been Deleted!'))
    return redirect('index')