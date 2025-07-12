from models.digrama_model import DiagramaDispersion

class DiagramaController:
    def __init__(self):
        self.model = DiagramaDispersion()

    def graficar_dispersion(self):
        try:
            self.model.generar_diagrama()
            print("📈 Gráfico de dispersión generado correctamente.")
        except Exception as e:
            print(f"Error al generar el gráfico de dispersión: {e}")