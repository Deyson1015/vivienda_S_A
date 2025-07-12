import pandas as pd
from tabulate import tabulate
from models.base_model import BaseModel
from models.tipo_vivienda_model import TipoViviendaModel
from config.config import COLLECTION_NAME

class EstadisticasVivienda:
    def __init__(self):
        self.vivienda_model = BaseModel(COLLECTION_NAME)
        self.tipo_model = TipoViviendaModel()

    def mostrar_resumen_estadistico(self):
        viviendas = self.vivienda_model.obtener_viviendas()
        if not viviendas:
            print("No hay datos en la colección de viviendas.")
            return

        df = pd.DataFrame(viviendas)

        # Calcular estadísticas
        total_viviendas = len(df)
        df["precio_m2"] = df["precio"] / df["area"]
        promedio_precio_m2 = df["precio_m2"].mean()

        # Obtener nombres de tipos de vivienda por id
        tipos = self.tipo_model.obtener_tipos()
        tipo_dict = {str(t["_id"]): t["nombre"] for t in tipos}
        df["tipo"] = df["id_tipo_vivienda"].astype(str).map(tipo_dict)

        # Clasificación por tipo de vivienda
        clasificacion = df["tipo"].value_counts().reset_index()
        clasificacion.columns = ["Tipo de Vivienda", "Cantidad"]

        # Mostrar resumen
        print("📊 RESUMEN ESTADÍSTICO")
        print(f"\n🏠 Total de viviendas registradas: {total_viviendas}")
        print(f"💰 Promedio del precio por metro cuadrado: ${promedio_precio_m2:,.2f}")
        print("\n📌 Clasificación por tipo de vivienda:")
        print(tabulate(clasificacion, headers="keys", tablefmt="grid"))
