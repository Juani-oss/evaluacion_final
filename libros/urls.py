from django.urls import path
from .views import *

urlpatterns = [
    path("", libro_list, name="libro_list"),
    path("libros/<int:id>", libro_detail, name="libro_detail"),
    path("libro/create", libro_create, name="libro_create"),
    path("libros/update/<int:id>", libro_update, name="libro_update"),
    path("libros/delete/<int:id>", libro_delete, name="libro_delete"),
]