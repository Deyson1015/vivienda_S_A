import pandas as pd
from tabulate import tabulate

class DataUtil:

    @staticmethod
    def preparar_dataframe(viviendas, tipos):
        if not viviendas:
            print("No hay datos en la colección de viviendas.")
            return None

        # Convertir lista de viviendas a DataFrame
        df = pd.DataFrame(viviendas)

        # Validar que existan columnas necesarias
        if "precio" not in df.columns or "area" not in df.columns:
            print("Faltan campos 'precio' o 'area' en los documentos.")
            return None

        # Limpiar y preparar datos
        df = df.dropna(subset=["precio", "area"])
        df = df[df["area"] > 0]
        df["precio_m2"] = df["precio"] / df["area"]

        # Crear diccionario de tipo de vivienda {id: nombre}
        tipo_dict = {str(t["_id"]): t["nombre"].upper() for t in tipos}
        df["tipo"] = df["id_tipo_vivienda"].astype(str).map(tipo_dict)

        # Asignar el nombre del tipo de vivienda al DataFrame
        df["nombre"] = df["id_tipo_vivienda"].astype(str).map(tipo_dict)

        return df
    
    @staticmethod
    def resumir_estadisticas(df, modelo_regresion):
        if df is None or df.empty:
            print("No hay datos disponibles para generar estadísticas.")
            return

        # Métricas básicas
        total_viviendas = len(df)
        promedio_precio_m2 = df["precio_m2"].mean()

        # Clasificación por tipo de vivienda
        clasificacion = df["tipo"].value_counts().reset_index()
        clasificacion.columns = ["Tipo de Vivienda", "Cantidad"]

        # Mostrar el resumen
        print("\n📊 RESUMEN ESTADÍSTICO")
        print(f"🏠 Total de viviendas registradas: {total_viviendas}")
        print(f"💰 Promedio del precio por metro cuadrado: ${promedio_precio_m2:,.2f}")
        print("\n📌 Clasificación por tipo de vivienda:")
        print(tabulate(clasificacion, headers="keys", tablefmt="grid"))
        
