from datetime import datetime

POSTS = [
    {
        "id": 1,
        "title": "Flip perfeito na Avenida Paulista",
        "slug": "flip-perfeito-avenida-paulista",
        "date": datetime(2025, 11, 1, 16, 30),
        "author": "Lia Souza",
        "category": "Street",
        "cover": "/static/img/flip.jpg",
        "summary": "Como treinar variações de flip e acertar no piso liso da Paulista.",
        "content": "Detalhes de setup, velocidade, posicionamento do pé da frente e corpo."
    },
    {
        "id": 2,
        "title": "Guia de spots clássicos em São Paulo",
        "slug": "guia-spots-classicos-sp",
        "date": datetime(2025, 10, 20, 10, 15),
        "author": "Rafa Lima",
        "category": "Guia",
        "cover": "/static/img/spots.jpg",
        "summary": "Os spots mais icônicos e como chegar neles sem perrengue.",
        "content": "Mapa, linhas possíveis, horários menos movimentados, dicas de segurança."
    },
    {
        "id": 3,
        "title": "Como escolher seu shape",
        "slug": "como-escolher-seu-shape",
        "date": datetime(2025, 9, 5, 18, 0),
        "author": "Duda Nunes",
        "category": "Gear",
        "cover": "/static/img/shape.jpg",
        "summary": "Largura, concave, wheelbase e o que realmente muda no seu rolê.",
        "content": "Testes práticos, materiais e quando trocar seu shape."
    },
]

CATEGORIES = sorted({p["category"] for p in POSTS})
AUTHORS = sorted({p["author"] for p in POSTS})
SITE = {
    "name": "SkaUnderCulture",
    "description": "Blog de skate com guias, técnicas e spots de São Paulo.",
}
