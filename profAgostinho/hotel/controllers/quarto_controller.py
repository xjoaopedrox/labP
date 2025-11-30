from models.quartos_model import get_quartos, alterar_status

def listar_quartos():
    return get_quartos()

def atualizar_status_limpeza(numero, status):
    alterar_status(numero, status)
