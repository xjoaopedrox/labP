from extensions import db
from models.quartos_model import Quarto

def listar_quartos():
    return Quarto.query.all()

def atualizar_status_limpeza(numero, status):
    quarto = Quarto.query.filter_by(numero=numero).first()
    if quarto:
        quarto.status = status
        db.session.commit()
