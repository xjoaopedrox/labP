class ObraLiteraria:
    def __init__(self, nome:str, escritor:str, paginas:int):
        self.nome = nome
        self.escritor = escritor
        self.paginas = paginas
        
    def exibir_info(self):
        print(f"Nome: {self.nome}\nEscritor: {self.escritor}\nTotal de páginas: {self.paginas}\n")
    

colecao = [
    {"nome": "O Guarani", "escritor": "José de Alencar", "qtde_paginas": 250},
    {"nome": "Iracema", "escritor": "José de Alencar", "qtde_paginas": 210},
    {"nome": "Dom Casmurro", "escritor": "Machado de Assis", "qtde_paginas": 256}
]

for obra in colecao:
    item = ObraLiteraria(obra["nome"], obra["escritor"], obra["qtde_paginas"])
    item.exibir_info()
s