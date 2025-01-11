from flet import Page

# Pages
from pages.Home import Home
from pages.parte_1.capitulo_3.ejercicio_18.Solucion import Ejercicio18

def get(page: Page = None):
    return [
        {
            'path': '/',
            'title': 'Home',
            'component': Home(page)
        },
        {
            'path': '/ejercicio_18',
            'title': 'POO - Ejercicio 18',
            'component' : Ejercicio18(page)
        }
]