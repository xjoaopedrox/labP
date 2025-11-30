from flask import request, make_response, redirect, session

def alternar_tema():
    tema_atual = request.cookies.get("tema", "claro")
    novo_tema = "escuro" if tema_atual == "claro" else "claro"

    if "usuario" in session:
        destino = "/dashboard"
    else:
        destino = "/"

    resposta = make_response(redirect(destino))
    resposta.set_cookie("tema", novo_tema, max_age=60*60*24*30)
    return resposta
