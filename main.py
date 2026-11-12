# Nosso código principal
from flask import Flask, render_template

app = Flask(__name__)

"""
Antes de iniciar os cálculos, o usuário deverá informar:
- Tamanho da residência em metros quadrados (m²).
- Quantidade de moradores.
- Tipo de residência (casa ou apartamento).
- Quantidade de banheiros.
- Existência de piscina (opcional).
"""
def calcular_custo_ambiental(tamanho, quantidade_moradores, tipo, quantidade_banheiros, piscina):
    coe_tamanho = 10
    coe_quantidade_morador = 5
    coe_quantidade_banheiros = 3
    coe_piscina = 8
    if tipo == "casa":
        coe_tipo = 10
    elif tipo == "apartamento":
        coe_tipo = 5

    return tamanho * coe_tamanho


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/consumo-de-energia")
def energia():
    return render_template("energia.html")

@app.route("/consumo-de-agua")
def agua():
    return render_template("agua.html")

@app.route("/volume-de-lixo")
def lixo():
    return render_template("lixo.html")

@app.route("/resultados")
def resultados():
    return render_template("resultados.html")

app.run(debug=True)