from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "segredo098"

grupo1 = [
    "Qual é o maior oceano do mundo?|A) Atlântico|B) Índico|C) Pacífico|D) Ártico|C",
    "Quem foi o primeiro homem a pisar na Lua?|A) Yuri Gagarin|B) Neil Armstrong|C) Buzz Aldrin|D) John Glenn|B",
    "Qual país é conhecido como 'Terra do Sol Nascente'?|A) China|B) Japão|C) Coreia do Sul|D) Tailândia|B",
    "Qual é o idioma oficial da Austrália?|A) Inglês|B) Francês|C) Alemão|D) Espanhol|A",
    "Qual é o maior deserto do mundo?|A) Saara|B) Kalahari|C) Atacama|D) Antártico|D"
]

grupo2 = [
    "Quem inventou a lâmpada elétrica?|A) Nikola Tesla|B) Thomas Edison|C) Alexander Graham Bell|D) Benjamin Franklin|B",
    "Qual é o planeta mais próximo do Sol?|A) Vênus|B) Mercúrio|C) Marte|D) Terra|B",
    "Qual é a moeda oficial do Reino Unido?|A) Euro|B) Libra Esterlina|C) Dólar|D) Franco|B",
    "Quem pintou a Mona Lisa?|A) Michelangelo|B) Leonardo da Vinci|C) Rafael|D) Botticelli|B",
    "Qual é o maior país em território?|A) Canadá|B) Rússia|C) China|D) EUA|B"
]

grupo3 = [
    "Qual é o elemento químico representado por 'O'?|A) Ouro|B) Oxigênio|C) Ósmio|D) Óxido|B",
    "Quantos ossos tem o corpo humano adulto?|A) 106|B) 206|C) 306|D) 406|B",
    "Qual é a capital da Argentina?|A) Buenos Aires|B) Córdoba|C) Rosário|D) Mendoza|A",
    "Quem escreveu 'A Divina Comédia'?|A) Dante Alighieri|B) Homero|C) Shakespeare|D) Cervantes|A",
    "Qual é o continente onde fica o Egito?|A) Ásia|B) África|C) Europa|D) América|B"
]

grupo4 = [
    "Qual é o maior rio do mundo em extensão?|A) Nilo|B) Amazonas|C) Yangtzé|D) Mississipi|A",
    "Quem criou a teoria da relatividade?|A) Isaac Newton|B) Albert Einstein|C) Galileo Galilei|D) Stephen Hawking|B",
    "Qual é a capital de Portugal?|A) Porto|B) Lisboa|C) Coimbra|D) Faro|B",
    "Qual é o animal símbolo da Austrália?|A) Canguru|B) Koala|C) Emu|D) Ornitorrinco|A",
    "Qual é o esporte mais popular do Brasil?|A) Vôlei|B) Futebol|C) Basquete|D) Handebol|B"
]

colecoes = [grupo1, grupo2, grupo3, grupo4]


@app.route("/")
def inicio():
    return """
    <h1>Menu de Jogos</h1>
    <a href='/sorteio'>Número Aleatório</a><br>
    <a href='/palavra'>Jogo da Forca</a><br>
    <a href='/tiro'>Campo de Tiro</a><br>
    <a href='/perguntas'>Quiz</a><br>
    <a href='/torre'>Torre de Hanoi</a><br>
    """

@app.route("/sorteio", methods=["GET", "POST"])
def sorteio():
    if "num_sorteado" not in session:
        session["num_sorteado"] = random.randint(1, 100)

    aviso = ""

    if request.method == "POST":
        try:
            tentativa = int(request.form["tentativa"])
            alvo = session["num_sorteado"]

            if tentativa == alvo:
                aviso = "Você acertou!"
                session.pop("num_sorteado")
            elif tentativa < alvo:
                aviso = "O número é maior" if alvo - tentativa < 10 else "Está bem mais alto"
            else:
                aviso = "O número é menor" if tentativa - alvo < 10 else "Está bem mais baixo"
        except:
            aviso = "Digite um valor válido."

    return render_template("numero.html", msg=aviso)

