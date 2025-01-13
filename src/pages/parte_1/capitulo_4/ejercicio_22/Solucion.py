from flet import Page, Column, Text, TextField, Container, ElevatedButton, AlertDialog, FontWeight
import locale
from .Empleado import Empleado

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

class Ejercicio22:
    def __init__(self, page: Page):
        self.page = page
        
        # Campos del formulario
        self.empleado_name_field = TextField(label="Nombre del empleado")
        self.empleado_horas_trabajadas_field = TextField(label="Horas trabajadas", suffix_text="Horas")
        self.empleado_valor_hora_field = TextField(label="Valor de la hora", suffix_text="COP", prefix_text="$", on_change=self.__format_currency)
        
        # Botón de cálculo
        self.calcular_button = ElevatedButton(text="Calcular salario", on_click=self.__generate_empleado)

    def __show_dialog_result(self, empleado: Empleado) -> None:
        show_text = f"El nombre del empleado es {empleado.nombre}"
        salario_empleado =  empleado.calcular_salario()
        
        if salario_empleado > 450_000:
            show_text += f" y el salario es de {locale.currency(salario_empleado, grouping=True)}"
        
        dlg = AlertDialog(
            modal=True,
            title=Text("Resultado"),
            content=Container(
                padding=40,
                content=Column(
                    tight=True,
                    controls=[
                        Text(f"{show_text}")
                    ]
                )
            ),
            actions=[
                ElevatedButton(text="Aceptar", on_click=lambda e: self.page.close(dlg))
            ]
        )
        
        self.page.open(dlg)
        
    def __generate_empleado(self, e) -> None:
        valor_hora = float(self.empleado_valor_hora_field.value.replace(",", ""))
        
        empleado = Empleado(nombre=self.empleado_name_field.value, horas=float(self.empleado_horas_trabajadas_field.value), valor_hora=valor_hora)
        
        self.__show_dialog_result(empleado)
        
        self.__reset_fields()
        
    def __format_currency(self, e) -> None:
        # Obtiene el valor actual sin separadores
        raw_value = self.empleado_valor_hora_field.value.replace(",", "")
        
        # Valida que sea numérico antes de formatear
        if raw_value.isdigit():
            # Formatea el valor con separadores de miles
            formatted_value = "{:,}".format(int(raw_value))
            self.empleado_valor_hora_field.value = formatted_value
            self.empleado_valor_hora_field.update()

    def __reset_fields(self) -> None:
        self.empleado_name_field.value = ""
        self.empleado_horas_trabajadas_field.value = ""
        self.empleado_valor_hora_field.value = ""
        self.empleado_name_field.update()
        self.empleado_horas_trabajadas_field.update()
        self.empleado_valor_hora_field.update()
    
    def render(self) -> Column:
        return Container(
            content=Column(
                controls=[
                    self.empleado_name_field,
                    self.empleado_horas_trabajadas_field,
                    self.empleado_valor_hora_field,
                    self.calcular_button
                ]
            )
        )

