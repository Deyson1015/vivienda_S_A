from models.base_model import BaseModel
from config.config import COLLECTION_NAME

class DatasetModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)

    def insertar_viviendas(self, lista_viviendas):
        try:
            if self.collection is None:
                print("No se pudo obtener la colección de viviendas.")
                return []

            resultado = self.collection.insert_many(lista_viviendas)
            print(f"Se insertaron {len(resultado.inserted_ids)} viviendas.")
            return resultado.inserted_ids
        except Exception as e:
            print(f"Error al insertar viviendas: {e}")
            return []