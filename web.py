# web_vivienda.py
from flask import Flask, render_template
from controllers.vivienda_controller import ViviendaController

app = Flask(__name__)
vc = ViviendaController()

@app.route('/')
def index():
    datos = vc.obtener_viviendas()
    return render_template('viviendas.html', datos=datos)

def grafica():
    datos = vc.obtener_viviendas() 
    return render_template('grafica.html')

def estadisticas():
    datos = vc.obtener_viviendas()  
    return render_template('estadisticas.html')

if __name__ == '__main__':
    app.run(debug=True)

