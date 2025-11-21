from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.secret_key = "segredo789"  

cadastro = {
    "Joao": {
        "email": "joaozinho@gmail.com",
        "senha": "senha123",
        "perfil": "Aluno",
        "descricao": "Aluno dedicado com boas notas",
        "genero": "Masculino",
        "registro": "RA2025001",
        "disciplina": "Matemática",
        "orientador": "Maria"
    },

    "Ana": {
        "email": "ana.estudante@gmail.com",
        "senha": "pythonlover",
        "perfil": "Aluno",
        "descricao": "Aluno com dificuldades, precisa melhorar",
        "genero": "Feminino",
        "registro": "RA2025002",
        "disciplina": "Biologia",
        "orientador": "Carlos"
    },

    "Marcos": {
        "email": "profmarcos@gmail.com",
        "senha": "prof2025",
        "perfil": "Professor",
        "descricao": "Docente experiente",
        "genero": "Masculino",
        "registro": "RA2025003",
        "disciplina": "Programação",
        "orientador": "Ele mesmo"
    }
}


@app.route("/")
def inicio():
    if "usuario" in session:
        return redirect(url_for("painel"))
    return redirect(url_for("entrar"))


@app.route("/entrar", methods=["GET", "POST"])
def entrar():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        if nome in cadastro and cadastro[nome]["senha"] == senha and cadastro[nome]["email"] == email:
            session["usuario"] = nome
            return redirect(url_for("painel"))
        else:
            return render_template("login.html", erro="Dados incorretos, tente novamente.")

    return render_template("login.html")


@app.route("/painel")
def painel():
    if "usuario" not in session:
        return redirect(url_for("entrar"))
    
    usuario = session["usuario"]
    dados = cadastro[usuario] 

    return render_template("info.html", usuario=usuario, dados=dados)


@app.route("/sair")
def sair():
    session.pop("usuario")
    return redirect(url_for("entrar"))


if __name__ == "__main__":
    app.run(debug=True)
