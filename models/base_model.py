from data.conexion import Conexion

class BaseModel:
    def __init__(self, collection_name):
        db = Conexion().obtener_conexion()
        if db is not None:
            self.collection = db[collection_name]
        else:
            self.collection = None
            print("No se pudo obtener la colección.")

    def insertar_viviendas(self, datos):
        if self.collection is not None:
            return self.collection.insert_one(datos).inserted_id
        else:
            print("No se pudo insertar.")
            return None

    def obtener_viviendas(self):
        if self.collection is not None:
            return list(self.collection.find())
        else:
            print("No se pudo obtener documentos.")
            return []

    def eliminar_todo(self):
        if self.collection is not None:
            resultado = self.collection.delete_many({})
            print(f"🗑️ {resultado.deleted_count} documentos eliminados.")
            return resultado.deleted_count
        else:
            print("No se pudo acceder a la colección.")
            return 0
