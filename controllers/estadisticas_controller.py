import pandas as pd
from tabulate import tabulate
from models.estadisticas_model import EstadisticasViviendaModel
from models.tipo_vivienda_model import TipoViviendaModel
from models.regresion_model import RegresionModel
from utils.data_util import DataUtil

class EstadisticasController:
    def __init__(self):
        self.vivienda_model = EstadisticasViviendaModel()
        self.tipo_model = TipoViviendaModel()
        self.regresion_model = RegresionModel()

    def mostrar_resumen(self):
        viviendas = self.vivienda_model.obtener_viviendas()
        tipos = self.tipo_model.obtener_tipos()
        df = DataUtil.preparar_dataframe(viviendas, tipos)

        if df is None:
            print(" No hay datos disponibles.")
            return

        total_viviendas = len(df)
        promedio_precio_m2 = df["precio_m2"].mean()

        clasificacion = df["tipo"].value_counts().reset_index()
        clasificacion.columns = ["Tipo de Vivienda", "Cantidad"]

        self.regresion_model.cargar_modelo()
        prediccion = self.regresion_model.predecir(100)

        # Mostrar
        print(" RESUMEN ESTADÍSTICO")
        print(f"\n Total de viviendas registradas: {total_viviendas}")
        print(f" Promedio del precio por metro cuadrado: ${promedio_precio_m2:,.2f}")
        print(f" Predicción del precio para una vivienda de 100 m²: ${prediccion:,.2f}")
        print("\n Clasificación por tipo de vivienda:")
        print(tabulate(clasificacion, headers="keys", tablefmt="grid"))
