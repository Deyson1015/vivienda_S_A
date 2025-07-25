from flask import Flask, render_template

# Controladores
from Backend.controllers.dataset_controller import DatasetController
from Backend.controllers.diagrama_controller import DiagramaController
from Backend.controllers.estadisticas_controller import EstadisticasController
from Backend.controllers.regresion_controller import RegresionController
from Backend.controllers.tipo_vivienda_controller import TipoViviendaController
from Backend.controllers.vivienda_controller import ViviendaController

# Utilidades
from Backend.utils.file_util import FileUtil

# Crear las carpetas necesarias para el proyecto
FileUtil.crear_carpetas()

# Limpiar datos antiguos
tv_controller = TipoViviendaController()
tv_controller.limpiar_tipos()

vivienda_controller = ViviendaController()
vivienda_controller.limpiar_viviendas()

# Insertar datos desde el dataset
dataset_controller = DatasetController()
dataset_controller.insertar_viviendas()

# Inicializar controlador de estadísticas
estadisticas_controller = EstadisticasController()
estadisticas_controller.mostrar_resumen()

# Crear la aplicación Flask
app = Flask(__name__, template_folder='Frontend/templates', static_folder='Frontend/static')

@app.route('/')
def inicio():
    return estadisticas_controller.mostrar_dashboard()

@app.route('/estadisticas')
def estadisticas():
    return estadisticas_controller.mostrar_resumen_web()

@app.route('/datos')
def viviendas():
    return vivienda_controller.obtener_viviendas_web()

@app.route('/grafico')
def grafica():
    diagrama = DiagramaController()
    return diagrama.generar_diagrama()

if __name__ == '__main__':
    app.run(debug=True)
