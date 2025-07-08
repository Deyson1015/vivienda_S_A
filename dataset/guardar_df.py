import pandas as pd
from tabulate import tabulate

ruta = 'C:/laragon/www/Machine Learnig/vivienda_S_A/dataset/dataset_vivienda.xlsx'
df = pd.read_excel(ruta, header=None)

print(tabulate(df.head(11), tablefmt='grid'))