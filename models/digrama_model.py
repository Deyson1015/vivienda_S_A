import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') 
import seaborn as sns
from models.base_model import BaseModel
from models.tipo_vivienda_model import TipoViviendaModel
from config.config import COLLECTION_NAME
from utils.data_util import DataUtil

class DiagramaDispersion(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)
        self.model = TipoViviendaModel()

    def generar_diagrama(self):
        viviendas = self.obtener_viviendas()
        tipos = self.model.obtener_tipos()
        df = DataUtil.preparar_dataframe(viviendas, tipos)

        if df is None:
            return "No hay datos suficientes para generar el diagrama."

        # Gráfico de dispersión
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=df,
            x="precio",
            y="precio_m2",
            hue="tipo",
            palette="Set1",
            alpha=0.7,
            s=60
        )
        plt.title("Dispersión: Precio vs Precio por m² según tipo de vivienda")
        plt.xlabel("Precio total de la vivienda")
        plt.ylabel("Precio por metro cuadrado")
        plt.grid(True)
        plt.tight_layout()
        plt.legend(title="Tipo de Vivienda")
        plt.savefig("dispersión_vivienda.png")
        plt.close()
