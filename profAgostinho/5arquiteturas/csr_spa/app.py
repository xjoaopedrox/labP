from flask import Flask, jsonify, render_template

app = Flask(__name__)

POSTS = [
    {"title": "A essência do street skate", "text": "O street skate é sobre criatividade e liberdade."},
    {"title": "A evolução das manobras", "text": "As manobras cresceram junto com a cultura do skate."},
    {"title": "Por que o skate é estilo de vida", "text": "Skate é atitude, comunidade e expressão."}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    return jsonify(POSTS)

if __name__ == "__main__":
    app.run(debug=True)
