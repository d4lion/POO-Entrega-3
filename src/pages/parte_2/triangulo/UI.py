from flet import (Page, TextField, ElevatedButton, 
                  Column, Row, Container, BottomSheet,
                  MainAxisAlignment, Colors, TextStyle, Icons, IconButton)

from .Triangulo import Triangulo

class TrianguloUI:
    def __init__(self, page: Page):
        self.page = page
        
        self.base_text_field = TextField(
            label='Base del Triángulo', 
            suffix_text='cm'
        )
        
        self.altura_text_field = TextField(
            label='Altura del Triángulo', 
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
        
    def __data_banner(self, trinagulo: Triangulo) -> BottomSheet:
        return BottomSheet(
            content=Container(
                padding=60,
                content=Column(
                    tight=True,
                    controls=[
                        self.__create_result_row("Área del Triángulo", f"{trinagulo.calcularArea():.2f} cm²"),
                        self.__create_result_row("Perímetro del Triángulo", f"{trinagulo.calcularPerimetro():.2f} cm"),
                        self.__create_result_row("Hipotenusa del Triángulo", f"{trinagulo.calcularHipotenusa():.2f} cm"),
                        self.__create_result_row("Tipo de Triángulo", trinagulo.determinarTipoDeTriangulo())
                    ]
                )
            )
        )
    
    def __calcular(self) -> None:
        base = float(self.base_text_field.value)
        altura = float(self.altura_text_field.value)
        self.page.open(self.__data_banner(Triangulo(base, altura)))
        
    def render(self) -> Container:
        return Container(
            padding=20,
            content=Column(
                tight=True,
                controls=[
                    self.base_text_field,
                    self.altura_text_field,
                    self.calcular_button
                ]
            )
        )