class Empleado:
    def __init__(self, nombre: str, horas: float, valor_hora: float):
        self.nombre = nombre
        self.horas = horas
        self.valor_hora = valor_hora
        
    def calcular_salario(self):
        return self.valor_hora * self.horas