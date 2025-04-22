"""Split Vehicles DataFrame into Series"""
import pandas as pd

# Create DataFrame
df = pd.DataFrame(data={'brand':['Chevrolet', 'Ford', 'Ducatti', 'BMW'],'model':['Corvette C5', 'Explorer 4x4', 'H100', 'Z05'],'type':['Car', 'SUV', 'Sportive Motocycle', 'Car'], 'year':[2005, 1999, 2012, 2010], 'color':['Yellow', 'Vine', 'Metallic Green', 'DeepBlue']})

# Split dataframe into series
models = df['model']
brands = df['brand']
types = df['type']
years = df['year']
colors = df['color']

# Set models Series to be the next index
df.index = models
df = df.drop(columns=['model']) # Drop model column, because it is being used as index, not as column

# Set dataframe data
df.data = {'brand':brands, 'type':types, 'year':years, 'color':colors}
print(df)