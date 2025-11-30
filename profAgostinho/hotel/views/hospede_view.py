from flask import render_template, session, redirect
from models.dados_iniciais import reservas

def hospede_dashboard():
    # Verifica login
    if "usuario" not in session:
        return redirect("/")
    usuario = session["usuario"]
    if usuario.get("perfil") != "Hóspede":
        return "Acesso negado", 403

    reservas_do_hospede = [r for r in reservas if r.get("hospede") == usuario.get("nome")]

    contexto = {
        "usuario": usuario,
        "reservas": reservas_do_hospede
    }
    return render_template("hospede.html", **contexto)
