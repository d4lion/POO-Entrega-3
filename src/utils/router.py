from flet import Page, View, Column, Text, RouteChangeEvent, ThemeMode, AppBar, IconButton


class Router:
    def __init__(self, page: Page, routes: list[dict[str:dict]] = [], 
                 app_bar: AppBar | None =None, WIDTH=1000, HEIGHT=600, WINDOW_RESIZABLE=True, 
                 WINDOW_MAXIMIZABLE=False, ALWAYS_ON_TOP=False, THEME_MODE=ThemeMode.LIGHT):
        
        self.routes = routes
        self.page = page
        self.app_bar = app_bar
        self.theme_mode = THEME_MODE
        
        self.SunnyButton: IconButton = self.app_bar.actions[0]
        
        self.SunnyButton.on_click = lambda e: self.change_theme()
        
        # Page config
        self.page.appbar = self.app_bar
        self.page.window.width = WIDTH
        self.page.window.height = HEIGHT
        self.page.window.resizable = WINDOW_RESIZABLE
        self.page.window.maximizable = WINDOW_MAXIMIZABLE
        self.page.window.always_on_top = ALWAYS_ON_TOP
        self.page.theme_mode = self.theme_mode
        
        # Routers Confing
        self.page.on_route_change = self._render_route
        
        try: 
            self.page.title = self.routes[0].get('title')
            self.page.add(
                self.routes[0].get('component').render()
            )
        except Exception as e:
            raise Exception("Debes crear almenos una ruta para renderizar la aplicación", e)
        
    def change_theme(self):        
        if self.page.theme_mode == ThemeMode.LIGHT:
            self.page.theme_mode = ThemeMode.DARK
            self.SunnyButton.icon = "wb_sunny"
        else:
            self.page.theme_mode = ThemeMode.LIGHT
            self.SunnyButton.icon = "wb_sunny_outlined"
        self.page.update()
        
    def _get_route_component(self, path: str) -> dict:
        for route in self.routes:
            if route.get('path') == path:
                return (route.get('title'), route.get('component'))
            
        return "Error not found"
        
    def _render_route(self, RouteEvent: RouteChangeEvent):
        try:
            title, component = self._get_route_component(RouteEvent.route)
            self.page.views.clear()
            self.page.title = title
            self.page.views.append(
                View(
                    RouteEvent.route,
                    [
                        self.app_bar,
                        component.render()
                    ]
                )
            )
        except Exception as e:
            self.page.views.append(
                View(
                    RouteEvent.route,
                    [
                        self.app_bar,
                        Column(controls=[Text("404 Not Found")])
                    ]
                )
            )
            raise Exception("Error al renderizar la ruta", e)
        finally:
            self.page.update()