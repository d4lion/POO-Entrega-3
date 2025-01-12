import locale

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato_social):
        self.pago_base = 50_000
        self.pago_matricula = self.pago_base
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social
        
    def calcular_pago(self) -> str:
        if (self.patrimonio > 2_000_000) and (self.estrato_social > 3):
            self.pago_matricula = self.pago_base + (0.03 * self.patrimonio)
        
        return f"El estudiante con numero de inscripcion {self.numero_inscripcion} y nombre {self.nombres} debe pagar {locale.currency(self.pago_matricula, grouping=True)}" 