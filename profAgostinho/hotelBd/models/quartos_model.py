from extensions import db

class Quarto(db.Model):
    __tablename__ = "quartos"
    numero = db.Column(db.String(10), primary_key=True)
    status = db.Column(db.String(50), nullable=False)
