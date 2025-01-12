from flet import Column, TextField, Button, Page, BottomSheet, Container, Text, AlertDialog

from .Estudiante import Estudiante


class Ejercicio10:
    def __init__(self, page: Page):
        self.page = page
        self.name_field = TextField(label="Nombre")
        self.patrimonio_field = TextField(
            label="Patrimonio", 
            suffix_text="COP", 
            prefix_text="$",
            on_change=self.format_currency  # Agregar el evento on_change
        )
        self.estrato_field = TextField(label="Estrato")
        self.numero_inscripcion_field = TextField(label="Numero de inscripción")
        self.button = Button(text="Calcular", on_click=self.show_dialog)
        
    def format_currency(self, e):
        # Obtiene el valor actual sin separadores
        raw_value = self.patrimonio_field.value.replace(",", "")
        
        # Valida que sea numérico antes de formatear
        if raw_value.isdigit():
            # Formatea el valor con separadores de miles
            formatted_value = "{:,}".format(int(raw_value))
            self.patrimonio_field.value = formatted_value
            self.patrimonio_field.update()
        
    def calcular_pago_estudiante(self, e) -> str:
        patrimonio = float(self.patrimonio_field.value.replace(",", ""))
        
        estudiante = Estudiante(
            nombres=self.name_field.value,
            patrimonio=patrimonio,
            estrato_social=int(self.estrato_field.value),
            numero_inscripcion=self.numero_inscripcion_field.value
        )
        
        return estudiante.calcular_pago()

    async def show_dialog(self, e):
        await self.page.show_dialog_async(
            dialog=AlertDialog(
                content=Container(
                    padding=40,
                    content=Column(
                        tight=True,
                        controls=[
                            Text(
                                value=self.calcular_pago_estudiante(None)
                            )
                        ]
                    )
                ),
                actions=[
                    Button(
                        text="Aceptar",
                        on_click=lambda e: self.page.close_dialog())
                ]
            )
        )

    def render(self):
        return Column(
            controls=[
                self.name_field,
                self.patrimonio_field,
                self.estrato_field,
                self.numero_inscripcion_field,
                self.button
            ]
        )
