import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

from models.regresion_model import RegresionModel
from controllers.dataset_controller import DatasetController
from config.config import IMAGENS_PATH

class DiagramaController:
    def __init__(self):
        self.dataset = DatasetController()

    def generar_diagrama(self):
        df = self.dataset.obtener_dataframe()

        if df is None:
            return "No hay datos suficientes para generar el diagrama."

        modelo = RegresionModel()
        modelo.entrenar_modelo(df[["precio_m2"]], df["precio"])
        modelo.cargar_modelo()
        df["prediccion"] = modelo.model.predict(df[["precio_m2"]])

        colores = {
            "CASA": "#F30909",         # rojo oscuro
            "APARTAMENTO": "#03039C",  # azul oscuro
            "OTRO": "#2ca02c"          # verde
        }

        formatear = ticker.FuncFormatter(lambda x, _: f"${x:,.0f}")

        plt.figure(figsize=(12, 7))

        sns.scatterplot(data=df, x="precio_m2", y="precio", hue="nombre", palette=colores, s=70, alpha=0.8, edgecolor='w', linewidth=0.5)

        sns.lineplot(x=df["precio_m2"], y=df["prediccion"], color='red', label='Regresión lineal')

        plt.gca().xaxis.set_major_formatter(formatear)
        plt.gca().yaxis.set_major_formatter(formatear)

        plt.title("Dispersión: Precio vs Precio por m² según tipo de vivienda")
        plt.xlabel("Precio por metro cuadrado")
        plt.ylabel("Precio total de la vivienda")
        plt.grid(True)
        plt.legend(title="Tipo de Vivienda")

        plt.tight_layout()
        plt.savefig(IMAGENS_PATH, format='png')
        plt.close()
        print("Diagrama generado y guardado correctamente.")
