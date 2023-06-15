from django.shortcuts import render
from .models import Task

from django.shortcuts import render
def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'auth_site/index.html', {'title': 'main site', 'tasks': tasks})

def about(request):
    return render(request, 'auth_site/about.html')

