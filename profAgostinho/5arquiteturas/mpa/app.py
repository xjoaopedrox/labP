from flask import Flask, render_template

app = Flask(__name__)

POSTS = [
    {"id": 1, "title": "A essência do street skate", "text": "O street skate é sobre criatividade e liberdade."},
    {"id": 2, "title": "A evolução das manobras", "text": "As manobras cresceram junto com a cultura do skate."},
    {"id": 3, "title": "Por que o skate é estilo de vida", "text": "Skate é atitude, comunidade e expressão."}
]

@app.route("/")
def index():
    return render_template("index.html", posts=POSTS)

@app.route("/post/<int:id>")
def post(id):
    post = next((p for p in POSTS if p["id"] == id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
