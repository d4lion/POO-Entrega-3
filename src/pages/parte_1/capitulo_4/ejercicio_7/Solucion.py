from flet import Page, TextField, Column, Button, BottomSheet, Container, TextStyle, Colors

class Ejercicio7:
    def __init__(self, page: Page):
        self.page = page
        self.text_fielda_A = TextField(
            label="Ingrese el valor de A",
        )
        self.text_fielda_B = TextField(
            label="Ingrese el valor de B",
        )

    def __algoritmo_propuesto(self, valor_A: float, valor_B: float):
        if valor_A > valor_B:
            return f"A es mayor que B"
        else:
            if valor_A == valor_B:
                return f"A es igual a B"
            else:
                return f"A es menor que B"
                    
        
    def render(self) -> Column:
        return Column(
        controls=[
            self.text_fielda_A,
            self.text_fielda_B,
            Button(
                text="Calcular",
                on_click=lambda e: self.page.show_dialog(
                    dialog=BottomSheet(
                        content=Container(
                            padding=60,
                            content=Column(
                                tight=True,
                                controls=[
                                    TextField(
                                        label="Resultado",
                                        value=self.__algoritmo_propuesto(
                                            float(self.text_fielda_A.value),
                                            float(self.text_fielda_B.value)
                                        ),
                                        disabled=True,
                                        bgcolor=Colors.WHITE,
                                        text_style=TextStyle(
                                            color=Colors.BLACK
                                        )
                                    )
                                ]
                            )
                        )
                    )
                )
            )
        ]
    )