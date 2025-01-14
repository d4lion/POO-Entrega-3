from math import pow

class Triangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        
    def calcularArea(self) -> float:
        return (self.base * self.altura) / 2
    
    def calcularHipotenusa(self) -> float:
        return pow(pow(self.base, 2) + pow(self.altura, 2), 0.5)
    
    def calcularPerimetro(self) -> float:
        return self.base + self.altura + self.calcularHipotenusa()
    
    def determinarTipoDeTriangulo(self) -> str:
        hipotenusa = self.calcularHipotenusa()
        
        if self.base == self.altura == hipotenusa:
            return "Es un triángulo equilátero"  # Todos sus lados son iguales
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Es un triángulo escaleno"  # Todos sus lados son diferentes
        else:
            return "Es un triángulo isósceles"  # De otra manera, es isósceles 