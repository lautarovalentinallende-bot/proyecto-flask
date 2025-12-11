from flask import Flask
import random

app = Flask(__name__)

datos = [
    "Los pulpos tienen tres corazones.",
    "La miel nunca se pudre.",
    "Los gatos duermen en promedio 15 horas al día.",
    "El Monte Everest crece unos milímetros cada año.",
]

@app.route('/')
def inicio():
    dato = random.choice(datos)
    return f"<h1>Hola, ¿cómo están?</h1><p>Dato random: {dato}</p>"
if __name__ == '__main__':
    app.run(debug=False)
