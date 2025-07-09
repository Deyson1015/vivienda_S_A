from pymongo import MongoClient, errors
from config.config import MONGO_URL, DB_NAME, COLLECTION_NAME, COLLECTION_NAME_2

class Conexion:
    def __init__(self):
        try:
            # Conectar a MongoDB usando las configuraciones del archivo config.py
            self.cliente = MongoClient(MONGO_URL)
            self.db = self.cliente[DB_NAME]
            self.collection = self.db[COLLECTION_NAME]
            self.collection_2 = self.db[COLLECTION_NAME_2]  

            self.conexion_exitosa = True
            print("Conexión exitosa a MongoDB.")
        
        except errors.ServerSelectionTimeoutError as e:
            self.conexion_exitosa = False
            print("No se pudo conectar a MongoDB. Verifica que el servidor esté en ejecución.")
            print(f"Error: {e}")

    def insertar(self, documento):
        if self.conexion_exitosa:
            self.collection.insert_one(documento)
        else:
            print("No se puede insertar: conexión no establecida.")

    def obtener_viviendas(self):
        if self.conexion_exitosa:
            return list(self.collection.find())
        else:
            print("No se pueden obtener datos: conexión no establecida.")
            return []

    def obtener_tipo_vivienda(self):
        if self.conexion_exitosa:
            return list(self.collection_2.find())
        else:
            print("No se pueden obtener datos: conexión no establecida.")
            return []
