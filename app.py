from controllers.vivienda_controller import ViviendaController
from controllers.tipo_vivienda_controller import TipoViviendaController
from controllers.dataset_controller import DatasetController
from controllers.estadisticas_controller import EstadisticasController
from controllers.diagrama_controller import DiagramaController
from controllers.regresion_controller import RegresionController

tv_controller = TipoViviendaController()
tv_controller.limpiar_tipos() # Elimina tipos
vc = ViviendaController()
vc.limpiar_viviendas()  # Elimina todo

dc = DatasetController()
dc.insertar_viviendas()  # Vuelve a insertar

modelo = RegresionController()
modelo.entrenar_modelo() # Entrena el modelo

estadisticas = EstadisticasController()
estadisticas.mostrar_resumen()

diadrama = DiagramaController()
diadrama.generar_diagrama()  # Genera el diagrama de dispersión 
