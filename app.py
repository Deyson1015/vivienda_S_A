from controllers.vivienda_controller import ViviendaController
from controllers.tipo_vivienda_controller import TipoViviendaController
from controllers.dataset_controller import DatasetController

tv_controller = TipoViviendaController()
tv_controller.eliminar_tipos() # Elimina tipos
vc = ViviendaController()
vc.eliminar_todas_las_viviendas()  # Elimina todo

dc = DatasetController()
dc.importar_viviendas()  # Vuelve a insertar
