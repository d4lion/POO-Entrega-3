class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado
        
    def calcularArea(self) -> float:
        return self.lado ** 2
    
    def calcularPerimetro(self) -> float:
        return 4 * self.lado
