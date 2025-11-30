from models.reservas_model import nova_reserva
from models.dados_iniciais import reservas

def listar_reservas():
    return reservas

def criar_reserva(nome, quarto):
    nova_reserva(nome, quarto)
