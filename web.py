# web_vivienda.py
from flask import Flask, render_template
from controllers.vivienda_controller import ViviendaController

app = Flask(__name__)
vc = ViviendaController()

@app.route('/')
def index():
    datos = vc.obtener_viviendas()  # Esto ya llama al modelo y consulta Mongo
    return render_template('viviendas.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
