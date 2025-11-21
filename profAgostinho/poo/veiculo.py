class Transporte:
    def __init__(self, fabricante: str, versao: str):
        self.fabricante = fabricante
        self.versao = versao

    def mostrar_info(self):
        return f"Fabricante: {self.fabricante}\nVersão: {self.versao}"
    
class Automovel(Transporte):
    def __init__(self, fabricante: str, versao: str, portas: int):
        super().__init__(fabricante, versao)  
        self.portas = portas

    def mostrar_info(self):
        return f"{super().mostrar_info()}\nQuantidade de portas: {self.portas}"
    
class Motocicleta(Transporte):
    def __init__(self, fabricante: str, versao: str, motor:int):
        super().__init__(fabricante, versao)
        self.motor = motor

    def mostrar_info(self):
        return f"{super().mostrar_info()}\nCilindradas: {self.motor}"

lista_carros = [
    {"fabricante": "Toyota", "versao": "Corolla",  "portas": 4},
    {"fabricante": "Honda", "versao": "Civic",  "portas": 4},
    {"fabricante": "Ford", "versao": "Mustang",  "portas": 2},
    {"fabricante": "Chevrolet", "versao": "Onix",  "portas": 4},
    {"fabricante": "Volkswagen", "versao": "Golf GTI",  "portas": 4}
]

lista_motos = [
    {"fabricante": "Honda", "versao": "CG 160", "motor": 160},
    {"fabricante": "Yamaha", "versao": "Fazer 250", "motor": 250},
    {"fabricante": "Kawasaki", "versao": "Ninja 400", "motor": 400},
    {"fabricante": "BMW", "versao": "G 310 R", "motor": 310},
    {"fabricante": "Suzuki", "versao": "GSX-S750", "motor": 750}
]

for carro in lista_carros:
    obj_carro = Automovel(carro['fabricante'], carro['versao'], carro['portas'])
    print(f"{obj_carro.mostrar_info()}\n")

for moto in lista_motos:
    obj_moto = Motocicleta(moto['fabricante'], moto['versao'], moto['motor'])
    print(f"{obj_moto.mostrar_info()}\n")
