# Nosso código principal
from flask import Flask, render_template

app = Flask(__name__)


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