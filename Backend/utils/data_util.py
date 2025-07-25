import pandas as pd
from tabulate import tabulate

class DataUtil:

    @staticmethod
    def preparar_dataframe(viviendas, tipos):
        if not viviendas:
            print("No hay datos en la colección de viviendas.")
            return None

        # Convertir lista de viviendas a DataFrame
        df = pd.DataFrame(viviendas)

        # Validar que existan columnas necesarias
        if "precio" not in df.columns or "area" not in df.columns:
            print("Faltan campos 'precio' o 'area' en los documentos.")
            return None

        # Limpiar y preparar datos
        df = df.dropna(subset=["precio", "area"])
        df = df[df["area"] > 0]
        df["precio_m2"] = df["precio"] / df["area"]

        # Crear diccionario de tipo de vivienda {id: nombre}
        tipo_dict = {str(t["_id"]): t["nombre"].upper() for t in tipos}
        df["tipo"] = df["id_tipo_vivienda"].astype(str).map(tipo_dict)

        # Asignar el nombre del tipo de vivienda al DataFrame
        df["nombre"] = df["id_tipo_vivienda"].astype(str).map(tipo_dict)

        return df
    
    @staticmethod
    def resumir_estadisticas(df, modelo_regresion):
        if df is None or df.empty:
            print("No hay datos disponibles para generar estadísticas.")
            return

        # Métricas básicas
        total_viviendas = len(df)
        promedio_precio_m2 = df["precio_m2"].mean()

        # Clasificación por tipo de vivienda
        clasificacion = df["tipo"].value_counts().reset_index()
        clasificacion.columns = ["Tipo de Vivienda", "Cantidad"]

        # Mostrar el resumen
        print("\n📊 RESUMEN ESTADÍSTICO")
        print(f"🏠 Total de viviendas registradas: {total_viviendas}")
        print(f"💰 Promedio del precio por metro cuadrado: ${promedio_precio_m2:,.2f}")
        print("\n📌 Clasificación por tipo de vivienda:")
        print(tabulate(clasificacion, headers="keys", tablefmt="grid"))
        
    @staticmethod
    def generar_estadisticas(df, modo='resumen'):
        if df is None:
            return {}

        if modo == 'resumen':
            total_viviendas = len(df)
            
            # Promedio del precio por metro cuadrado
            promedio_precio_m2 = df["precio_m2"].mean()

            casas = df[df["tipo"] == "CASA"].shape[0]
            apartamentos = df[df["tipo"] == "APARTAMENTO"].shape[0]
            otros = total_viviendas - (casas + apartamentos)
            
            # Promedio del precio total de las viviendas
            promedio_precio_total = df["precio"].mean()

            # Precio mínimo y máximo
            precio_min = df["precio"].min()
            precio_max = df["precio"].max()

            # Promedio de área
            promedio_area = df["area"].mean()

            # Rango de precios
            rango_precio = f"${precio_min:,.0f} - ${precio_max:,.0f}"

            # Desviación estándar del precio
            desviacion_precio = df["precio"].std()

            # Desviación estándar del área
            desviacion_area = df["area"].std()

            # Promedio de habitaciones (si existe en tu dataset)
            promedio_habitaciones = df["habitaciones"].mean() if "habitaciones" in df.columns else "N/A"

            # Número de viviendas con precio superior al promedio
            viviendas_precio_superior = len(df[df["precio"] > promedio_precio_total])

            # Número de viviendas con área superior al promedio
            viviendas_area_superior = len(df[df["area"] > promedio_area])

            # Número de viviendas con más de 3 habitaciones (solo si el campo 'habitaciones' está presente)
            viviendas_mas_3_habitaciones = len(df[df["habitaciones"] > 3]) if "habitaciones" in df.columns else "N/A"

            # Agregar otros valores adicionales
            return {
                "total_viviendas": total_viviendas,
                "promedio_precio_m2": f"${promedio_precio_m2:,.0f}",
                "promedio_precio_total": f"${promedio_precio_total:,.0f}",
                "precio_min": f"${precio_min:,.0f}",
                "precio_max": f"${precio_max:,.0f}",
                "rango_precio": rango_precio,
                "promedio_area": f"{promedio_area:,.2f} m²",
                "desviacion_precio": f"${desviacion_precio:,.0f}",
                "desviacion_area": f"{desviacion_area:,.2f} m²",
                "promedio_habitaciones": f"{promedio_habitaciones:,.2f}",
                "viviendas_precio_superior": viviendas_precio_superior,
                "viviendas_mas_3_habitaciones": viviendas_mas_3_habitaciones,
                "casas": casas,
                "apartamentos": apartamentos,
                "otros": otros,
            }

        elif modo == 'dashboard':
            total_viviendas = len(df)
            precio_promedio = df['precio'].mean()
            area_promedio = df['area'].mean()
            precio_m2_promedio = df['precio_m2'].mean()

            clasificacion = df['tipo'].value_counts().reset_index()
            clasificacion.columns = ['Tipo', 'Cantidad']
            casas = df[df["tipo"] == "CASA"].shape[0]
            apartamentos = df[df["tipo"] == "APARTAMENTO"].shape[0]
            otros = total_viviendas - (casas + apartamentos)
            porcentaje_casas = round((casas / total_viviendas) * 100, 2)
            porcentaje_apartamentos = round((apartamentos / total_viviendas) * 100, 2)
            porcentaje_otros = round((otros / total_viviendas) * 100, 2)
            precio_min = f"{df['precio'].min():,.0f}"
            precio_max = f"{df['precio'].max():,.0f}"
            area = df["area"].mode().iloc[0] if not df["area"].mode().empty else "No disponible"

            return {
                "total_viviendas": total_viviendas,
                "precio_promedio": f"${precio_promedio:,.0f}",
                "area_promedio": f"{area_promedio:,.2f} m² ",
                "precio_m2_promedio": f"${precio_m2_promedio:,.0f}",
                "casas": casas,
                "apartamentos": apartamentos,
                "otros": otros,
                "porcentaje_casas": porcentaje_casas,
                "porcentaje_apartamentos": porcentaje_apartamentos,
                "porcentaje_otros": porcentaje_otros,          
                "precio_min": precio_min,
                "precio_max": precio_max,
                "area": area
            }

        else:
            print(f"Modo desconocido: {modo}")
            return {}