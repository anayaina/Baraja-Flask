from flask import Flask, render_template
import tarjetas, pares
app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html",carta1="/static/images/back_purple.png",carta2="/static/images/back_red.png")

@app.route("/game_on")
def game_on():
    jugadorA,jugadorB,ganador=pares.jugar_web()
    return render_template("game_on.html",jugador1=jugadorA,jugador2=jugadorB,winner=ganador)