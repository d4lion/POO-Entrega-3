from math import pi, pow

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
        
    def calcularArea(self) -> float:
        return pi * pow(self.radio, 2)
    
    def calcularPerimetro(self) -> float:
        return 2 * pi * self.radio