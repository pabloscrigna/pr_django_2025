from django.urls import path

from .views import alumnos_vista

urlpatterns = [
    path("", alumnos_vista)
]