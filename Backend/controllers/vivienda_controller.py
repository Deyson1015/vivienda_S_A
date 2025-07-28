from Backend.models.vivienda_model import ViviendaModel
from Backend.controllers.tipo_vivienda_controller import TipoViviendaController
from config.config import COLLECTION_NAME
from flask import render_template

class ViviendaController:
    def __init__(self):
        self.model = ViviendaModel(COLLECTION_NAME)
        self.tipo = TipoViviendaController()

    def obtener_viviendas(self):
        try:
            viviendas = self.model.obtener_viviendas()
            print(f" Se obtuvieron {len(viviendas)} viviendas.")
            return viviendas
        except Exception as e:
            print(f" Error al obtener viviendas: {e}")
            return []
        
    def obtener_viviendas_web(self):
        try:
            viviendas = self.model.obtener_viviendas()

            for idx, vivienda in enumerate(viviendas, start=1):
                tipo_id = vivienda.get('id_tipo_vivienda', None)  # Obtener el ID del tipo de vivienda
                
                # Obtener el nombre del tipo de vivienda usando obtener_id_tipo
                tipo_vivienda = self.tipo.obtener_id_tipo(tipo_id) if tipo_id else 'Desconocido'

                if tipo_vivienda:
                    vivienda['tipo_vivienda'] = tipo_vivienda['nombre']  
                else:
                    vivienda['tipo_vivienda'] = 'Desconocido'  

                vivienda['_id'] = idx

                vivienda['precio'] = f"${vivienda['precio']:,.0f}"
                vivienda['fecha_publicacion'] = vivienda['fecha_publicacion'].strftime("%Y-%m-%d") if vivienda['fecha_publicacion'] else "Fecha no disponible"
                vivienda['fecha_construccion'] = vivienda['fecha_construccion'].strftime("%Y-%m-%d") if vivienda['fecha_construccion'] else "Fecha no disponible"
            if not viviendas:
                return render_template("datos.html", mensaje="No hay viviendas registradas.")
            return render_template("datos.html", viviendas=viviendas)  
        except Exception as e:
            print(f" Error al obtener viviendas: {e}")
            return render_template("datos.html", mensaje=f"Hubo un error al obtener las viviendas. Detalles: {e}")
  
    def limpiar_viviendas(self):
        try:
            eliminados = self.model.eliminar_todo()
            print(f"Se eliminaron {eliminados} viviendas.")
            return eliminados
        except Exception as e:
            print(f"Error al eliminar viviendas: {e}")
            return 0
