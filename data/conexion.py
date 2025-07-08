from pymongo import MongoClient, errors

class Conexion:
    def __init__(self, db_name, collection_name):
        try:
            self.cliente = MongoClient('mongodb://localhost:27017/')  
            self.db = self.cliente[db_name]
            self.collection = self.db[collection_name]
            self.conexion_exitosa = True
            print(" Conexión exitosa a MongoDB.")
        
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


