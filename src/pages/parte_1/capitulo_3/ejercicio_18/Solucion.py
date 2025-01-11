from flet import (TextField, ElevatedButton, AlertDialog, Container, TextButton, Text, Ref, 
                  Page, DataTable, DataColumn, DataRow, DataCell, Column, Row)

from .Empleado import Empleado

class Ejercicio18:
    def __init__(self, page: Page):
        self.page = page
        self.lista_empleados: list[Empleado] = []
        self.dialog_ref = Ref[AlertDialog]()
        
        self.__init_text_fields()
        self.__init_buttons()
        self.__init_dialog()

    def __init_text_fields(self):
        self.text_field_empleado_name = TextField(label="Nombre del empleado")
        self.text_field_empleado_id = TextField(label="ID de empleado")
        self.text_field_empleado_worked_hours = TextField(label="Horas trabajadas")
        self.text_field_empleado_payment_per_hour = TextField(label="Pago por hora")
        self.text_field_empleado_taxes = TextField(label="Introduce los impuestos (como decimal, ej: 0.2)")

    def __init_buttons(self):
        self.button_crear_empleado = ElevatedButton(
            text="Crear empleado", on_click=self.crear_empleado)
        self.button_lista_empleados = ElevatedButton(
            text="Mostrar empleados", on_click=self.mostrar_lista_empleados)

    def __init_dialog(self):
        self.dialog_ref.current = AlertDialog(
            title=Text("Lista de empleados"),
            content=Container(),
            actions=[TextButton("Cerrar", on_click=lambda e: self.page.close(self.dialog_ref.current))],
            scrollable=True,
            adaptive=True,
        )

    def generar_tabla_empleados(self):
        return DataTable(
            columns=[
                DataColumn(Text("Código empleado")),
                DataColumn(Text("Nombre")),
                DataColumn(Text("Salario bruto")),
                DataColumn(Text("Salario neto")),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text(str(empleado.id))),
                        DataCell(Text(empleado.name)),
                        DataCell(Text(f"{empleado.calcular_salario_bruto()}")),
                        DataCell(Text(f"{empleado.calcular_salario_neto()}")),
                    ]
                )
                for empleado in self.lista_empleados
            ],
        )

    def mostrar_lista_empleados(self, e):
        self.dialog_ref.current.content = self.generar_tabla_empleados()
        self.page.dialog = self.dialog_ref.current
        self.dialog_ref.current.open = True
        self.page.update()

    def crear_empleado(self, e) -> Empleado:
        try:
            empleado = Empleado(
                name=self.text_field_empleado_name.value,
                id=self.text_field_empleado_id.value,
                worked_hours=float(self.text_field_empleado_worked_hours.value),
                payment_per_hour=float(self.text_field_empleado_payment_per_hour.value),
                taxes=float(self.text_field_empleado_taxes.value),
            )
        except ValueError:
            assert("Error al crear empleado")

        self._clear_text_fields()
        self.lista_empleados.append(empleado)
        self.mostrar_lista_empleados(None)
        
        return empleado

    def _clear_text_fields(self):
        self.text_field_empleado_id.value = ""
        self.text_field_empleado_name.value = ""
        self.text_field_empleado_worked_hours.value = ""
        self.text_field_empleado_payment_per_hour.value = ""
        self.text_field_empleado_taxes.value = ""

    def render(self):
        return Column(
            controls=[
                Text("Registro de Empleados", style="headlineSmall"),
                self.text_field_empleado_name,
                self.text_field_empleado_id,
                self.text_field_empleado_worked_hours,
                self.text_field_empleado_payment_per_hour,
                self.text_field_empleado_taxes,
                Row(controls=[self.button_crear_empleado, self.button_lista_empleados]),
            ],
            scroll="always",
        )
