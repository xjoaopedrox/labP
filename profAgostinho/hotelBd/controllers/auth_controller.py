from flask import session
from models.usuarios_model import Usuario
from extensions import db

def login_usuario(email, senha):
    return Usuario.query.filter_by(email=email, senha=senha).first()

def logout_usuario():
    session.clear()
