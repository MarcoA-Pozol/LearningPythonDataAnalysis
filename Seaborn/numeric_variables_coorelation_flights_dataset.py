import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('./DataSets/flights_details.xls')

# Select numeric columns
numeric_cols = ['Passengers', 'Ticket Cost', 'Minutes', 'Distance (km)', 'Total Revenue', 
                'Fuel Consumption (liters)', 'CO2 Emissions (kg)', 'Load Factor (%)', 'Delay Minutes']

# Verify if not numeric values in columns
for col in numeric_cols:
    non_numeric = df[col].apply(lambda x: not str(x).replace('.', '').isdigit() if x == x else False)
    if non_numeric.any():
        print(f"Columna '{col}' tiene valores no numéricos:", df[col][non_numeric].unique())

# Clean data and replace '-' and other non numeric values like NaN 
df[numeric_cols] = df[numeric_cols].replace('-', pd.NA).apply(pd.to_numeric, errors='coerce')

corr_matrix = df[numeric_cols].corr()

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt=".2f")
plt.title('Numeric variables coorelation')
plt.show()