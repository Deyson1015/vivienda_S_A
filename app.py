from flask import Flask, render_template, request
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

regresion_controller = RegresionController()

# Crear la aplicación Flask
app = Flask(__name__, template_folder='Frontend/templates', static_folder='Frontend/static')

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return estadisticas_controller.mostrar_dashboard()

@app.route("/predicciones", methods=["GET", "POST"])
def predicciones():
    if request.method == "POST":
        return regresion_controller.procesar_prediccion()
    return render_template("predicciones.html") 


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

@app.errorhandler(404)
def not_found_error(e):
    return render_template("errores.html", error_code=404,
                           error_title="Página no encontrada",
                           error_message="La página que buscas no existe o fue eliminada."), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("errores.html", error_code=500,
                           error_title="Error interno del servidor",
                           error_message="Ocurrió un error inesperado en el servidor."), 500

@app.errorhandler(403)
def forbidden_error(e):
    return render_template("errores.html", error_code=403,
                           error_title="Acceso denegado",
                           error_message="No tienes permisos para acceder a esta página."), 403

@app.errorhandler(504)
def timeout_error(e):
    return render_template("errores.html", error_code=504,
                           error_title="Tiempo de espera agotado",
                           error_message="El servidor tardó demasiado en responder."), 504

if __name__ == '__main__':
    app.run(debug=True)
