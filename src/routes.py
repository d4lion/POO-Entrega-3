from flet import Page

# Pages
from pages.Home import Home
from pages.parte_1.capitulo_3.ejercicio_18.Solucion import Ejercicio18
from pages.parte_1.capitulo_3.ejercicio_19.Solucion import Ejercicio19
from pages.parte_1.capitulo_4.ejercicio_7.Solucion import Ejercicio7
from pages.parte_1.capitulo_4.ejercicio_10.Solucion import Ejercicio10
from pages.parte_1.capitulo_4.ejercicio_22.Solucion import Ejercicio22
from pages.parte_1.capitulo_4.ejercicio_23.Solucion import Ejercicio23

# Parte 2
from pages.parte_2.circulo.UI import CirculoUI
from pages.parte_2.cuadrado.UI import CuadradoUI
from pages.parte_2.rectangulo.UI import RectanguloUI
from pages.parte_2.triangulo.UI import TrianguloUI

def get(page: Page = None):
    return [
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
        },
        {
            'path': '/ejercicio_23',
            'title': 'POO - Ejercicio 23',
            'component' : Ejercicio23(page)
        },
        {
            'path': '/ejercicio_circulo',
            'title': 'POO - Ejercicio Circulo',
            'component' : CirculoUI(page)
        },
        {
            'path': '/ejercicio_cuadrado',
            'title': 'POO - Ejercicio Cuadrado',
            'component' : CuadradoUI(page)
        },
        {
            'path': '/ejercicio_rectangulo',
            'title': 'POO - Ejercicio Rectangulo',
            'component' : RectanguloUI(page)
        },
        {
            'path' : '/ejercicio_triangulo',
            'title': 'POO - Ejercicio Triangulo',
            'component' : TrianguloUI(page)
        }
]