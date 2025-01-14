from flet import (Page, TextField, ElevatedButton, 
                  Column, Row, Container, BottomSheet,
                  MainAxisAlignment, Colors, TextStyle, Icons, IconButton)

from .Cuadrado import Cuadrado

class CuadradoUI:
    def __init__(self, page: Page):
        self.page = page
        
        self.square_side = TextField(
            label='Lado del cuadrado', 
            suffix_text='cm'
        )
        
        self.calcular_button = ElevatedButton(
            text='Calcular', 
            on_click=lambda e: self.__calcular()
        )
        
    def __create_result_row(self, label: str, value: str) -> Row:
        return Row(
            controls=[
                TextField(
                    label=label,
                    value=value,
                    read_only=True,
                    bgcolor=Colors.WHITE,
                    text_style=TextStyle(color=Colors.BLACK)
                ),
                IconButton(
                    icon=Icons.COPY,
                    on_click=lambda e: self.page.set_clipboard(value)
                ),
            ],
            alignment=MainAxisAlignment.CENTER
        )
        
    def __data_banner(self, cuadrado: Cuadrado) -> BottomSheet:
        return BottomSheet(
            content=Container(
                padding=60,
                content=Column(
                    tight=True,
                    controls=[
                        self.__create_result_row("Área del cuadrado", f"{cuadrado.calcularArea():.2f} cm²"),
                        self.__create_result_row("Perímetro del cuadrado", f"{cuadrado.calcularPerimetro():.2f} cm"),
                    ]
                )
            )
        )
        
    def __calcular(self):
        side = float(self.square_side.value)
        self.page.open(self.__data_banner(Cuadrado(side)))
        
    def render(self):
        return Container(
            content=Column(
                controls=[
                    self.square_side,
                    self.calcular_button
                ]    
            )
        )