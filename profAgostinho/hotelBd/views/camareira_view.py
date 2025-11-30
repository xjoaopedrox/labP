from flask import render_template, session, redirect
from models.dados_iniciais import quartos

def camareira_dashboard():
    # Verifica login
    if "usuario" not in session:
        return redirect("/")
    usuario = session["usuario"]
    if usuario.get("perfil") != "Camareira":
        return "Acesso negado", 403

    contexto = {
        "quartos": quartos,
        "usuario": usuario
    }
    return render_template("camareira.html", **contexto)
