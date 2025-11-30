from flask import Flask, render_template
import time

app = Flask(__name__)

POSTS = [
    {"title": "A essência do street skate", "text": "O street skate é sobre criatividade e liberdade."},
    {"title": "A evolução das manobras", "text": "As manobras cresceram junto com a cultura do skate."},
    {"title": "Por que o skate é estilo de vida", "text": "Skate é atitude, comunidade e expressão."}
]

def generate_static():
    html = render_template("base.html", posts=POSTS, updated=time.ctime())
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

# Inicialmente gera o arquivo
generate_static()

@app.route("/")
def index():
    return open("index.html", "r", encoding="utf-8").read()

# Regenera manualmente
@app.route("/regen")
def regen():
    generate_static()
    return "Página regenerada!"

if __name__ == "__main__":
    app.run(debug=True)
