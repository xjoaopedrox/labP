from models.dados_iniciais import quartos

def get_quartos():
    return quartos

def alterar_status(numero, status):
    for quarto in quartos:
        if quarto["numero"] == numero:
            quarto["status"] = status
            return True
    return False
