from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, "libros/libro_list.html", {"libros": libros})

def libro_detail(request, id):
    libro = get_object_or_404(Libro, id=id)
    return render(request, "libros/libro_detail.html", {"libro": libro})

def libro_create(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libro_list")
    else:
        form = LibroForm()
        
    return render(request, "libros/libro_form.html", {"form": form})

def libro_update(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect("libro_list")
    else:
        form = LibroForm(instance=libro)
        
    return render(request, "libros/libro_form.html", {"form": form})

def libro_delete(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect("libro_list")