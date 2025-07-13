from datetime import datetime
from dateutil.relativedelta import relativedelta

class FechaUtil:
    @staticmethod
    def calcular_fecha_construccion(antiguedad):
    
        if not isinstance(antiguedad, (int, float)):
            return None
        
        try:
            fecha_actual = datetime.now()
            fecha_construccion = fecha_actual - relativedelta(years=int(antiguedad))
            return fecha_construccion.strftime("%Y-%m-%d")
        except Exception as e:
            print(f" Error al calcular fecha de construcción: {e}")
            return None
