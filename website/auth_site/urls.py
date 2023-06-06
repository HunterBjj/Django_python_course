from os import path

from . import views

urlpatterns = [
    path("", views.index, name="auth_site"),
]