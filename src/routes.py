from flet import Page

# Pages
from pages.Home import Home
from pages.parte_1.capitulo_3.ejercicio_18.Solucion import Ejercicio18
from pages.parte_1.capitulo_3.ejercicio_19.Solucion import Ejercicio19
from pages.parte_1.capitulo_4.ejercicio_7.Solucion import Ejercicio7
from pages.parte_1.capitulo_4.ejercicio_10.Solucion import Ejercicio10
from pages.parte_1.capitulo_4.ejercicio_22.Solucion import Ejercicio22

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
        },
        {
            'path': '/ejercicio_19',
            'title': 'POO - Ejercicio 19',
            'component' : Ejercicio19(page)
        },
        {
            'path': '/ejercicio_7',
            'title': 'POO - Ejercicio 7',
            'component' : Ejercicio7(page)
        },
        {
            'path': '/ejercicio_10',
            'title': 'POO - Ejercicio 10',
            'component' : Ejercicio10(page)
        },
        {
            'path': '/ejercicio_22',
            'title': 'POO - Ejercicio 22',
            'component' : Ejercicio22(page)
        }
]