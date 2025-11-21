from abc import ABC, abstractmethod
import math

class Figura(ABC):

    @abstractmethod
    def obter_area(self):
        pass

    @abstractmethod
    def obter_perimetro(self):
        pass


class Quadrilatero(Figura):
    def __init__(self, largura: float, comprimento: float):
        self.largura = largura
        self.comprimento = comprimento

    def obter_area(self):
        return self.largura * self.comprimento

    def obter_perimetro(self):
        return 2 * (self.largura + self.comprimento)


class Poligono3Lados(Figura):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def obter_area(self):
        semi_perimetro = self.obter_perimetro() / 2
        return math.sqrt(semi_perimetro * (semi_perimetro - self.a) * 
                         (semi_perimetro - self.b) * (semi_perimetro - self.c))

    def obter_perimetro(self):
        return self.a + self.b + self.c


formas_geometricas = [
    Quadrilatero(4, 8),
    Poligono3Lados(3, 4, 5),
    Quadrilatero(2, 6),
    Poligono3Lados(6, 7, 8)
]

for figura in formas_geometricas:
    print(f"{type(figura).__name__}:")
    print("  Área:", figura.obter_area())
    print("  Perímetro:", figura.obter_perimetro(), "\n")
