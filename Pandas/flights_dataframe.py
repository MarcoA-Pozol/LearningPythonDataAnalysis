import pandas as pd

# Load dataset
df = pd.read_csv("DataSets/flights_details.csv")
print(df.describe())