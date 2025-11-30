from models.dados_iniciais import usuarios

def buscar_usuario(email, senha):
    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            return u
    return None
