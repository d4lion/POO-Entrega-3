import flet as ft
import routes

class AppBar:
    def __init__(self, _routerGoTo):
        self._routerGoTo = _routerGoTo
        # Almacenar la lista de rutas desde routes.get()
        self.routes = routes.get()

    def render(self):
        # Generar dinámicamente los items para el PopupMenuButton
        menu_items = [
            ft.PopupMenuItem(
                text=route["title"], 
                on_click=lambda e, path=route["path"]: self._routerGoTo(path)
            )
            for route in self.routes
        ]

        return ft.AppBar(
            leading_width=30,
            title=ft.Text("Entrega POO 3", size=20, weight="bold"),
            center_title=False,
            actions=[
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
                ft.PopupMenuButton(items=menu_items)
            ]
        )
