import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

    def calcular_diametro(self):
        return 2 * self.raio


circ1 = Circulo(10)

print(f"Raio é {circ1.raio}. Suave.")
print(f"Area: {circ1.calcular_area():.3f}")
print(f"Perimetro: {circ1.calcular_perimetro():.3f}")
print(f"Diametro: {circ1.calcular_diametro()}")
