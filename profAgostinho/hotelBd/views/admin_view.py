from flask import render_template, session, redirect
from models.dados_iniciais import usuarios, quartos, reservas

def admin_dashboard():
    # Verifica login
    if "usuario" not in session:
        return redirect("/")
    usuario = session["usuario"]
    if usuario.get("perfil") != "Administrador":
        return "Acesso negado", 403

    # Dados que o admin precisa ver
    contexto = {
        "usuarios": usuarios,
        "quartos": quartos,
        "reservas": reservas,
        "usuario": usuario
    }
    return render_template("admin.html", **contexto)
