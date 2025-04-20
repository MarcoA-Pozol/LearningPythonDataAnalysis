import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Markdown

# Pandas display settings
def display_every_row_column(c_allow:bool=False, r_allow:bool=False):
    """
        Display every row and/or column in the dataframe output.

        Args:
            c_allow(bool): True or False to allow every column to be displayed in the output.
            r_allow(bool): True or False to allow every row to be displayed in output.

        Returns:
            None   
    """
    if c_allow:
        pd.set_option('display.max_columns', None) # Show all columns
    if r_allow:
        pd.set_option('display.max_rows', None) # Show all rows
    pass
display_every_row_column(c_allow=True, r_allow=False)

# Load dataset
df = pd.read_excel('./DataSets/flights_details.xls')
print(df)


""" Group average minutes of delay by airline """
# Clean non numeric data from Delay Minutes column
df['Delay Minutes'] = df['Delay Minutes'].replace('-', pd.NA).apply(pd.to_numeric, errors='coerce')

avg_delay_minutes_by_airline = df.groupby('Airline')['Delay Minutes'].mean()

# Convert Series to DataFrame and rename columns
avg_delay_minutes_by_airline = avg_delay_minutes_by_airline.reset_index()
avg_delay_minutes_by_airline.columns = ['Airline', 'Delay Minutes']

# Sort by desc order
avg_delay_minutes_by_airline = avg_delay_minutes_by_airline.sort_values(by='Delay Minutes', ascending=False)

# Adding title to the dataframe
title = '     Average Delay Minutes by Airline'
print(title)
print(avg_delay_minutes_by_airline)
