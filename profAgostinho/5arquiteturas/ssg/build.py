from jinja2 import Environment, FileSystemLoader

POSTS = [
    {"title": "A essência do street skate", "text": "O street skate é sobre criatividade e liberdade."},
    {"title": "A evolução das manobras", "text": "As manobras cresceram junto com a cultura do skate."},
    {"title": "Por que o skate é estilo de vida", "text": "Skate é atitude, comunidade e expressão."}
]

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("base.html")

html = template.render(posts=POSTS)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SSG gerado → index.html")
