"""Split a DataFrame into Series"""
import pandas as pd


df = pd.DataFrame(data={'name':['Jarid', 'Helena', 'Humberto', 'Angel', 'Dwayne'], 'age':[21, 19, 40, 64, 35], 'ocupation':['Medic', 'Dishwasher', 'Baker', 'Periodist', 'Engineer']})
print(df)

# Spliting dataframe into series
names = df['name']
ages = df['age']
ocupations = df['ocupation']
print(names, ages, ocupations)

# These are the same than the lists we have over, they are already pd.Series 
name_series = pd.Series(names)
age_series = pd.Series(ages)
ocupation_series = pd.Series(ocupations)

print(name_series, age_series, ocupation_series)

# Using name_series as custom index for a dataframe
df.index = name_series
df.data = {'age':age_series, 'ocupation':ocupation_series}
df = df.drop(columns=['name'])
print(df)