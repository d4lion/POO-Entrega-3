from flet import (Page, TextField, BottomSheet, Container, 
                  Column, Row, IconButton, Icons, Colors, Banner, MainAxisAlignment, Text, 
                  ElevatedButton, Icon, TextButton, TextStyle, FontWeight)

from .Triangulo import Triangulo

class Ejercicio19:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.__init_text_fields()
        
    async def calcular(self, e) -> None:
        try:
            t1 = Triangulo(float(self.lado_triangulo_text_field.value))
            self.lado_triangulo_text_field.value = ""
            await self.page.show_dialog_async(
                dialog=self.create_result_dialog(t1)
            )
        except ValueError:
            await self.page.show_banner_async(
                banner=self.create_error_banner()
            )
        finally:
            self.page.update()

    def create_result_dialog(self, triangulo: Triangulo) -> BottomSheet:
        return BottomSheet(
            content=Container(
                padding=60,
                content=Column(
                    tight=True,
                    controls=[
                        self.create_result_row("Área del triángulo", f"{triangulo.calcular_area():.2f} cm²"),
                        self.create_result_row("Perímetro del triángulo", f"{triangulo.calcular_perimetro():.2f} cm"),
                        self.create_result_row("Altura del triángulo", f"{triangulo.calcular_altura():.2f} cm"),
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )
        )

    def create_result_row(self, label: str, value: str) -> Row:
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

    def create_error_banner(self) -> Banner:
        err_banner = Banner(
            bgcolor=Colors.AMBER_100,
            leading=Icon(Icons.WARNING_AMBER_ROUNDED, color=Colors.AMBER, size=40),
            content=Text(
                value="Oops, parece que hubo un error, asegurate de ingresar un número",
                color=Colors.BLACK,
            ),
            actions=[
                TextButton(
                    text="close",
                    on_click=lambda e: self.page.close(err_banner)
                )
            ]
        )
        
        return err_banner
    
    def __init_text_fields(self) -> None:
        self.lado_triangulo_text_field = TextField(
        label='Lado',
        suffix_text='cm',
    )

        self.calc_button = ElevatedButton(
            text='Calcular',
            on_click=self.calcular
        )
        
    def render(self) -> Column:
        return Column(
        controls=[
            Text("Calcular el área de un triángulo equilatero, perimetro y su altura",
                    size=20, weight=FontWeight.W_300),
            self.lado_triangulo_text_field,
            self.calc_button
        ]
    )