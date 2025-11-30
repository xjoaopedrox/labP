from app import app
from extensions import db
from models.usuarios_model import Usuario
from models.quartos_model import Quarto
from models.reservas_model import Reserva

with app.app_context():
    if not Usuario.query.first():
        u1 = Usuario(nome="Admin", email="admin@hotel.com", senha="123", perfil="Administrador")
        u2 = Usuario(nome="João", email="recep@hotel.com", senha="123", perfil="Recepcionista")
        u3 = Usuario(nome="Maria", email="camareira@hotel.com", senha="123", perfil="Camareira")
        u4 = Usuario(nome="Carlos Hóspede", email="hospede@hotel.com", senha="123", perfil="Hóspede")
        db.session.add_all([u1, u2, u3, u4])
        db.session.commit()

    if not Quarto.query.first():
        q1 = Quarto(numero="101", status="Limpo")
        q2 = Quarto(numero="102", status="Sujo")
        q3 = Quarto(numero="103", status="Limpando")
        db.session.add_all([q1, q2, q3])
        db.session.commit()

    print("Banco populado com sucesso!")
