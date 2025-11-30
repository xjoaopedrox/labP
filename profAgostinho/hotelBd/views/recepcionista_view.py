from flask import render_template, session, redirect
from models.dados_iniciais import reservas, quartos

def recepcionista_dashboard():
    # Verifica login
    if "usuario" not in session:
        return redirect("/")
    usuario = session["usuario"]
    if usuario.get("perfil") != "Recepcionista":
        return "Acesso negado", 403

    contexto = {
        "reservas": reservas,
        "quartos": quartos,
        "usuario": usuario
    }
    return render_template("recepcionista.html", **contexto)
