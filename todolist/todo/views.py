from django.shortcuts import render, redirect, get_object_or_404
from .models import task  # Assuming your model is named Task, not task
from .forms import taskform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login


def home(request):
    t1 = task.objects.all()
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = taskform()

    return render(request, 'tasks.html', {"t1": t1,'form': form})

def todoform(request):
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = taskform()

    return render(request, 'tasks.html', {'form': form})

def delete_task(request,id):
    Task=get_object_or_404(task,id=id)
    if request.method=="POST":
        Task.delete()
        return redirect('home')

def task_update(request, pk):
    Task = get_object_or_404(task, pk=pk)
    if request.method == 'POST':
        form = taskform(request.POST, instance=Task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = taskform()
    return render(request, 'task_form.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            auth_login(request, form.instance)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

