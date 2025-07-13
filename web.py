# web_vivienda.py
from flask import Flask, render_template
from controllers.vivienda_controller import ViviendaController

app = Flask(__name__)
vc = ViviendaController()

@app.route('/')
def index():
    datos = vc.obtener_viviendas()
    return render_template('viviendas.html', datos=datos)

@app.route('/')
def grafica():
    datos = vc.obtener_viviendas() 
    return render_template('grafica.html')

@app.route('/dispersion')
def dispersion():
    return render_template('dispersion.html')

if __name__ == '__main__':
    app.run(debug=True)

