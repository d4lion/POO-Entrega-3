import flet as ft

from utils.router import Router

# Components
from components.App_bar import AppBar

# Routes
import routes

def main(page: ft.Page):
    Router(page=page, 
        routes=routes.get(page),
        app_bar=AppBar(page.go).render())
    

ft.app(main)
