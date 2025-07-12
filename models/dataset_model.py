import pandas as pd
from models.base_model import BaseModel
from models.tipo_vivienda_model import TipoViviendaModel
from config.config import COLLECTION_NAME, DATASET_PATH
from utils.texto_util import TextoUtil

class DatasetModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)
        self.tipo_model = TipoViviendaModel()

    def insertar_viviendas(self):
        if self.collection is None:
            print("No se pudo obtener la colección de viviendas.")
            return []

        try:
            df = pd.read_excel(DATASET_PATH)
            viviendas = df.to_dict(orient="records")

            tipos_unicos = set()
            viviendas_con_tipo = []

            for vivienda in viviendas:
                tipo_detectado = TextoUtil.limpiar_descripcion(vivienda.get("descripcion", ""))

                # Clasificación
                if tipo_detectado == "apartamento":
                    tipo = "Apartamento"
                elif tipo_detectado == "casa":
                    tipo = "Casa"
                else:
                    tipo = "Otro"

                tipos_unicos.add(tipo)

            # Insertar tipos únicos en la colección tipo_vivienda
            for tipo in tipos_unicos:
                self.tipo_model.insertar_tipo_unico(tipo)

            # Ahora volvemos a recorrer para insertar viviendas con id_tipo_vivienda
            for vivienda in viviendas:
                tipo_detectado = TextoUtil.limpiar_descripcion(vivienda.get("descripcion", ""))

                if tipo_detectado == "apartamento":
                    tipo = "Apartamento"
                elif tipo_detectado == "casa":
                    tipo = "Casa"
                else:
                    tipo = "Otro"

                id_tipo = self.tipo_model.obtener_id(tipo)
                vivienda["id_tipo_vivienda"] = id_tipo

                viviendas_con_tipo.append(vivienda)

            resultado = self.collection.insert_many(viviendas_con_tipo)
            print(f"Se insertaron {len(resultado.inserted_ids)} viviendas con tipo.")
            return resultado.inserted_ids

        except Exception as e:
            print(f"Error al insertar viviendas con tipo: {e}")
            return []
