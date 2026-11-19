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

def result_calculate(size, lights, device):
    """Calcula o consumo estimado com base na área, número de luminárias e aparelhos.

    Args:
        size (int): Tamanho (área) da residência
        lights (int): Quantidade de luminárias
        device (int): Quantidade de aparelhos

    Returns:
        float: Consumo estimado
    """
    # Coeficientes usados no cálculo do consumo de energia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/consumo-de-energia")
def energia():
    return render_template("energia.html")

# A segunda página de energia
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# A terceira página de energia
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )


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