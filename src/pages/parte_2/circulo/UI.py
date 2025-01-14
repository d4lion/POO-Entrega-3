from flet import (Container, Column, TextField, Page, ElevatedButton, 
                  Icons, IconButton, MainAxisAlignment, Colors, TextStyle, Row, BottomSheet)


from .Circulo import Circulo

class CirculoUI:
    def __init__(self, page: Page):
        self.page = page
        self.radio_textfield = TextField(label='Radio del círculo', suffix_text='cm')
        self.calcular_button = ElevatedButton(text='Calcular', on_click=lambda e: self.__calcular())
        
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
              
    def __data_banner(self, circulo: Circulo) -> BottomSheet:
        return BottomSheet(
            content=Container(
                padding=60,
                content=Column(
                    tight=True,
                    controls=[
                        self.__create_result_row("Área del círculo", f"{circulo.calcularArea():.2f} cm²"),
                        self.__create_result_row("Perímetro del círculo", f"{circulo.calcularPerimetro():.2f} cm"),
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )
        )
    
    def __calcular(self) -> None:
        radio = float(self.radio_textfield.value)
        self.page.open(self.__data_banner(Circulo(radio)))
    
    def render(self) -> Container:
        return Container(
            content=Column(
                controls=[
                    self.radio_textfield,
                    self.calcular_button
                ]
            )
        )