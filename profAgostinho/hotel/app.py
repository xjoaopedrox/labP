import os
import sys

from flask import Flask, render_template, request, redirect, session, make_response
from controllers.auth_controller import login_usuario, logout_usuario
from controllers.quarto_controller import listar_quartos, atualizar_status_limpeza
from controllers.reserva_controller import listar_reservas, criar_reserva
from models.dados_iniciais import usuarios, reservas, quartos
from controllers.theme_controller import alternar_tema

app = Flask(__name__)
app.secret_key = "segredo"


@app.route("/tema")
def tema():
    return alternar_tema()


@app.route("/", methods=["GET", "POST"])
def login():
    tema = request.cookies.get("tema", "claro")

    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        usuario = login_usuario(email, senha)

        if usuario:
            session["usuario"] = usuario
            return redirect("/dashboard")
        else:
            return render_template("login.html", erro="Login inválido", tema=tema)

    return render_template("login.html", tema=tema)


@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect("/")

    tema = request.cookies.get("tema", "claro")
    usuario = session["usuario"]
    perfil = usuario["perfil"]

    if perfil == "Administrador":
        return render_template("admin.html", usuarios=usuarios, tema=tema)

    if perfil == "Recepcionista":
        return render_template("recepcionista.html", reservas=reservas, quartos=quartos, tema=tema)

    if perfil == "Camareira":
        return render_template("camareira.html", quartos=quartos, tema=tema)

    if perfil == "Hóspede":
        return render_template("hospede.html", usuario=usuario, tema=tema)

    return "Perfil desconhecido"



@app.route("/logout")
def sair():
    logout_usuario()
    return redirect("/")



@app.route("/atualizar_limpeza", methods=["POST"])
def atualizar_limpeza():
    quarto = request.form.get("numero")
    status = request.form.get("status")
    atualizar_status_limpeza(quarto, status)
    return redirect("/dashboard")


@app.route("/nova_reserva", methods=["POST"])
def nova_reserva():
    nome = request.form.get("nome")
    quarto = request.form.get("quarto")
    criar_reserva(nome, quarto)
    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(debug=True)
