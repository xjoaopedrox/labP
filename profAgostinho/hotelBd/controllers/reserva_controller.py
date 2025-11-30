from extensions import db
from models.reservas_model import Reserva

def listar_reservas():
    return Reserva.query.all()

def criar_reserva(nome, numero_quarto):
    reserva = Reserva(hospede=nome, quarto=numero_quarto)
    db.session.add(reserva)
    db.session.commit()
