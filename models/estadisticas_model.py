import pandas as pd
from tabulate import tabulate
from models.base_model import BaseModel
from models.tipo_vivienda_model import TipoViviendaModel
from config.config import COLLECTION_NAME
from utils.data_util import DataUtil

class EstadisticasVivienda(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)
        self.model = TipoViviendaModel()

    def mostrar_resumen_estadistico(self):
        viviendas = self.obtener_viviendas()
        tipos = self.model.obtener_tipos()
        df = DataUtil.preparar_dataframe(viviendas, tipos)

        if df is None:
            return
        
        total_viviendas = len(df)
        promedio_precio_m2 = df["precio_m2"].mean()
        
        # Clasificación por tipo de vivienda
        clasificacion = df["tipo"].value_counts().reset_index()
        clasificacion.columns = ["Tipo de Vivienda", "Cantidad"]

        # Mostrar resumen
        print("📊 RESUMEN ESTADÍSTICO")
        print(f"\n🏠 Total de viviendas registradas: {total_viviendas}")
        print(f"💰 Promedio del precio por metro cuadrado: ${promedio_precio_m2:,.2f}")
        print("\n📌 Clasificación por tipo de vivienda:")
        print(tabulate(clasificacion, headers="keys", tablefmt="grid"))
