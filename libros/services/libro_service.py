import requests

from ..models import Libro

def get_libros():
    response = requests.get("https://openlibrary.org/search.json?subject=classics&limit=20")
    if response.status_code != 200:
        print(f"Error al obtener los libros:{response.status_code}")
        return[]

    return response.json()["docs"]

def load_libros():
    if Libro.objects.count():
        return f"ya existen {Libro.objects.count()}libros"
    libros = get_libros()
    for libro in libros:
        if "cover_i" not in libro:
            continue
        Libro.objects.create(
            title=libro["title"],
            description=", ".join(libro.get("author_name", [])),
            price=10,
            image=f"https://covers.openlibrary.org/b/id/{libro['cover_i']}-L.jpg",
        )

    return f"Se cargaron {Libro.objects.count()} libros"
