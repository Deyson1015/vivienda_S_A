from models.estadisticas_model import EstadisticasVivienda

class EstadisticasController:
    def __init__(self):
        self.model = EstadisticasVivienda()

    def mostrar_estadisticas(self):
        try:
            self.model.mostrar_resumen_estadistico()
            print("📊 Estadísticas calculadas correctamente.")
        except Exception as e:
            print(f"Error al calcular estadísticas: {e}")
            return
        