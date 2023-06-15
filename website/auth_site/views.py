from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request, 'auth_site/index.html')

def about(request):
    return render(request, 'auth_site/about.html')

