from flask import session
from models.usuarios_model import buscar_usuario


def login_usuario(email, senha):
    return buscar_usuario(email, senha)

def logout_usuario():
    session.clear()
