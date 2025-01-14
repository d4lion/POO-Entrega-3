class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
        
    def calcularArea(self) -> float:
        return self.base * self.altura
    
    def calcularPerimetro(self) -> float:
        return 2 * (self.base + self.altura)
        