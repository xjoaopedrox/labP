from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "segredo123"  # precisa pro flash e session

# Lista para armazenar usuários
# Obs: vai sumir se reiniciar o servidor, mas é o que o exercício quer
if "usuarios" not in globals():
    usuarios = []

@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # só adiciona se tudo estiver ok (JS já valida também)
        usuarios.append({
            "username": username,
            "email": email,
            "password": password
        })

        flash("Cadastro realizado com sucesso!")

        return redirect("/")

    return render_template("formulario.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
