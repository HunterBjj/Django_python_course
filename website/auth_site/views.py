from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect
def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'auth_site/index.html', {'title': 'main site', 'tasks': tasks})

def about(request):
    return render(request, 'auth_site/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была не верной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'auth_site/create.html')
