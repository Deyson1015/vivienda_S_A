from controllers.vivienda_controller import ViviendaController
from controllers.tipo_vivienda_controller import TipoViviendaController
from controllers.dataset_controller import DatasetController
from controllers.estadisticas_controller import EstadisticasController
from controllers.diagrama_controller import DiagramaController

tv_controller = TipoViviendaController()
tv_controller.eliminar_tipos() # Elimina tipos
vc = ViviendaController()
vc.eliminar_todas_las_viviendas()  # Elimina todo

dc = DatasetController()
dc.importar_viviendas()  # Vuelve a insertar

estadisticas = EstadisticasController()
estadisticas.mostrar_estadisticas()  

diadrama = DiagramaController()
diadrama.graficar_dispersion()  