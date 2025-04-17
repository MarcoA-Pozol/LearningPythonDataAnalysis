# Importamos pandas con el alias "pd"
import pandas as pd

# Cargamos el set de datos a partir de un archivo xls (Excel) en un dataframe de pandas
df = pd.read_excel("DataSets/flights_details.xls")

print(df) # Visualizamos el dataframe (Nos muestra los datos en un formato similar a una tabla)
print(df.describe()) # Nos muestra datos importantes de manera directa y sencilla como std, mean, max, min, etc