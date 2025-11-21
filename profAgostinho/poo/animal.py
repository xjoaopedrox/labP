class Animal:
    def __init__(self, nome: str):
        self.nome = nome
    
    def emitir_som(self):
        return "som generico"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"
    
    def latir(self):
        return "Woof woof!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
    def miar(self):
        return "Meow meow!"
    

dog = Cachorro("Rex")


cat = Gato("Luna")


print(f"{dog.nome} diz: {dog.emitir_som()}")
print(f"{dog.nome} também faz: {dog.latir()}")

print(f"{cat.nome} faz: {cat.miar()}")