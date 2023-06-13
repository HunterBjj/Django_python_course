
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='auth_site'),
    #path('about/', views.index(), name='about-club'),
]
