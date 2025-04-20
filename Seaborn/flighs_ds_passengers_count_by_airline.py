import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframe
df = pd.read_excel('./DataSets/flights_details.xls')
# print(df)

"""Group passengers count by airline"""
passengers_count_by_airline = df.groupby('Airline')['Passengers'].count() # Series

# Convert Series to DataFrame
passengers_count_by_airline = passengers_count_by_airline.reset_index()
passengers_count_by_airline.columns = ['Airline', 'Passengers'] # DataFrame

title = '\n####  Total passengers by Airline  ####\n'.upper()
separation_line = '-' * len(title)
print(title, separation_line)
print(passengers_count_by_airline)