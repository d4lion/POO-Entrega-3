from math import sqrt, pow

class Ecuacion:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def solve(self) -> tuple[float, float] | tuple[None, None]:
        try:
            determinante = sqrt(pow(self.b, 2) - 4 * self.a * self.c)
        except ValueError:
            return None, ValueError("El determinante es negativo")
                
        x1 = (-self.b + determinante) / (2 * self.a)
        x2 = (-self.b - determinante) / (2 * self.a)
        
        return x1, x2