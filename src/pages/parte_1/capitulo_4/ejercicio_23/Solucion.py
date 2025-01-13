from flet import Text, TextField, ElevatedButton, Column, Container, Page, AlertDialog, Row

from .Ecuacion import Ecuacion


class Ejercicio23:
    def __init__(self, page: Page):
        self.page = page
        
        # Crear los controles
        self.a_textfield = TextField(label="Valor de a")
        self.b_textfield = TextField(label="Valor de b")
        self.c_textfield = TextField(label="Valor de c")
        self.calcular_button = ElevatedButton("Calcular", on_click=self.__show_result)
    
    def __show_result(self, e):
        a = float(self.a_textfield.value)
        b = float(self.b_textfield.value)
        c = float(self.c_textfield.value)
        
        x1, x2 = Ecuacion(a, b, c).solve()
        
        print(x2)
        
        if x1 is not None:
            dlg = AlertDialog(
            title=Text("Resultado"),
            content=Container(
                padding=40,
                content=Column(
                    tight=True,
                    controls=[
                        Row(
                            controls=[
                                Text("Ecuación: ", size=18, weight="bold"),        
                                Text(f"{a}x^2 + {b}x + {c} = 0", size=18)
                            ]
                        ),
                        Column(
                            controls=[
                                Row(
                                    controls=[
                                        Text("x1: ", size=18, weight="bold"),
                                        Text(f"{x1}", size=18)
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Text("x2: ", size=18, weight="bold"),
                                        Text(f"{x2}", size=18)  
                                    ]
                                )
                            ]
                        )
                    ]   
                )
            ),
            actions=[
                ElevatedButton("Aceptar", on_click=lambda e: self.page.close(dlg))
            ]
        )
        else:
            dlg = AlertDialog(
                title=Text("Resultado"),
                content=Container(
                    padding=40,
                    content=Column(
                        tight=True,
                        controls=[
                            Text("La ecuación no tiene solución", size=18)
                        ]
                    )
                ),
                actions=[
                    ElevatedButton("Aceptar", on_click=lambda e: self.page.close(dlg))
                ]
            )
        
        self.page.open(dlg)
    
    
    def render(self) -> Container:
        return Container(
            content=Column(
                controls=[
                    Text("Ingrese los valores de a, b y c de la ecuación cuadrática ax^2 + bx + c = 0"),
                    self.a_textfield,
                    self.b_textfield,
                    self.c_textfield,
                    self.calcular_button
                ]
            )
        )
