from math import sqrt, pow

class Triangulo:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self) -> float:
        return (sqrt(3) / 4) * pow(self.lado, 2)

    def calcular_altura(self) -> float:
        return (sqrt(3) / 2) * self.lado

    def calcular_perimetro(self) -> float:
        return 3 * self.lado
