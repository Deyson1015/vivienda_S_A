import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from models.diagrama_model import DiagramaModel
from models.tipo_vivienda_model import TipoViviendaModel
from models.regresion_model import RegresionModel
from config.config import  IMAGENS_PATH
from utils.data_util import DataUtil

class DiagramaController:
    def __init__(self):
        self.vivienda_model = DiagramaModel()
        self.tipo_model = TipoViviendaModel()
        self.regresion_model = RegresionModel()

    def generar_diagrama(self):
        viviendas = self.vivienda_model.obtener_viviendas()
        tipos = self.tipo_model.obtener_tipos()
        df = DataUtil.preparar_dataframe(viviendas, tipos)

        if df is None:
            print(" No hay datos suficientes para generar el diagrama.")
            return

        self.regresion_model.cargar_modelo()
        X = df["area"].values.reshape(-1, 1)
        y = df["precio"].values
        y_pred = self.regresion_model.model.predict(X)

        # Crear diagrama
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, color="blue", label="Datos reales")
        plt.plot(X, y_pred, color="red", label="Línea de regresión")
        plt.xlabel("Área (m²)")
        plt.ylabel("Precio ($)")
        plt.title("Diagrama de dispersión con regresión")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(IMAGENS_PATH, format='png')
        plt.close()
        print(f" Diagrama guardado en {IMAGENS_PATH}")
