from data.conexion import Conexion

# Crear una instancia de la conexión
conexion = Conexion(db_name='viviendas_s_a', collection_name='vivienda')

# Verificar si la conexión fue exitosa
if conexion.conexion_exitosa:
    print("Conexión a MongoDB verificada correctamente.")
else:
    print("La conexión a MongoDB falló.")




