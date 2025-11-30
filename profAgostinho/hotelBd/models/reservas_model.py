from extensions import db

class Reserva(db.Model):
    __tablename__ = "reservas"
    id = db.Column(db.Integer, primary_key=True)
    hospede = db.Column(db.String(100), nullable=False)
    quarto = db.Column(db.String(10), nullable=False)
