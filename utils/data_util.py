import pandas as pd

class DataUtil:
        
    @staticmethod
    def preparar_dataframe(viviendas, tipos):
        if not viviendas:
            print("No hay datos en la colección de viviendas.")
            return None

        df = pd.DataFrame(viviendas)

        if "precio" not in df or "area" not in df:
            print(" Faltan campos 'precio' o 'area' en los documentos.")
            return None

        df = df.dropna(subset=["precio", "area"])
        df = df[df["area"] > 0]
        df["precio_m2"] = df["precio"] / df["area"]

        # Mapear tipo de vivienda
        tipo_dict = {str(t["_id"]): t["nombre"].upper() for t in tipos}
        df["tipo"] = df["id_tipo_vivienda"].astype(str).map(tipo_dict)

        return df
