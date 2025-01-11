import locale

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

class Empleado:
    def __init__(self, name: str, id: str | int, worked_hours: float, payment_per_hour: float, taxes: float):
        self.name = name
        self.id = id
        self.worked_hours = worked_hours
        self.payment_per_hour = payment_per_hour
        self.taxes = taxes

    def calcular_salario_neto(self) -> str:
        return locale.currency(self.worked_hours * self.payment_per_hour * (1 - self.taxes), grouping=True)

    def calcular_salario_bruto(self) -> str:
        return locale.currency(self.worked_hours * self.payment_per_hour, grouping=True)