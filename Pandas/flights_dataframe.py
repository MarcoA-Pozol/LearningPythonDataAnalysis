# Importamos pandas con el alias "pd"
import pandas as pd

# Load dataset in a pandas dataframe
df = pd.read_excel("../DataSets/flights_details.xls")

# Clasify data grouped by flight type
print(df.groupby(by=['Flight Type']))

