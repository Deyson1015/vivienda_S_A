# controllers/dataset_controller.py
import pandas as pd
from datetime import datetime
from models.dataset_model import DatasetModel
from models.tipo_vivienda_model import TipoViviendaModel
from utils.texto_util import TextoUtil
from utils.fecha_util import FechaUtil
from config.config import DATASET_PATH

class DatasetController:
    def __init__(self):
        self.model = DatasetModel()
        self.tipo_model = TipoViviendaModel()

    def insertar_viviendas(self):
        try:
            df = pd.read_excel(DATASET_PATH)
            viviendas = df.to_dict(orient="records")

            tipos_unicos = set()

            for vivienda in viviendas:
                tipo_detectado = TextoUtil.limpiar_descripcion(vivienda.get("descripcion", ""))
                tipo = "Apartamento" if tipo_detectado == "apartamento" else "Casa" if tipo_detectado == "casa" else "Otro"
                tipos_unicos.add(tipo)

            # Insertar tipos únicos en la base de datos
            for tipo in tipos_unicos:
                self.tipo_model.insertar_tipo_unico(tipo)

            viviendas_con_tipo = []
            for vivienda in viviendas:
                tipo_detectado = TextoUtil.limpiar_descripcion(vivienda.get("descripcion", ""))
                tipo = "Apartamento" if tipo_detectado == "apartamento" else "Casa" if tipo_detectado == "casa" else "Otro"
                fecha = FechaUtil.calcular_fecha_construccion(vivienda.get("antiguedad"))
                try:
                    fecha = datetime.strptime(fecha, "%Y-%m-%d") if fecha else None
                except Exception as e:
                    print(f"Error convirtiendo fecha: {fecha}")
                    fecha = None
                id_tipo = self.tipo_model.obtener_id(tipo)

                vivienda["descripcion"] = str(vivienda.get("descripcion", "")).upper()
                vivienda["fecha_construccion"] = fecha
                vivienda.pop("antiguedad", None)
                vivienda["id_tipo_vivienda"] = id_tipo

                viviendas_con_tipo.append(vivienda)

            self.model.insertar_varias_viviendas(viviendas_con_tipo)

        except Exception as e:
            print(f"Error en la carga del dataset: {e}")
            