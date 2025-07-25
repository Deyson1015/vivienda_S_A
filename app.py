from Backend.controllers.vivienda_controller import ViviendaController
from Backend.controllers.tipo_vivienda_controller import TipoViviendaController
from Backend.controllers.dataset_controller import DatasetController
from Backend.controllers.estadisticas_controller import EstadisticasController
from Backend.controllers.diagrama_controller import DiagramaController
from Backend.controllers.regresion_controller import RegresionController
from Backend.utils.file_util import FileUtil

# Crear las carpetas necesarias para el proyecto
FileUtil.crear_carpetas()

tv_controller = TipoViviendaController()
tv_controller.limpiar_tipos() # Elimina tipos
vc = ViviendaController()
vc.limpiar_viviendas()  # Elimina todo

dc = DatasetController()
dc.insertar_viviendas()  # Vuelve a insertar

estadisticas = EstadisticasController()
estadisticas.mostrar_resumen()

diadrama = DiagramaController()
diadrama.generar_diagrama()  # Genera el diagrama de dispersión 
