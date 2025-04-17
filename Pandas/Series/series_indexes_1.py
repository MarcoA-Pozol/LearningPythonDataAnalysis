"""Indexes in Series"""
import pandas as pd

"""First Example"""
cities = ['Detroit', 'Oklahoma', 'Nevada', 'Houston', 'New York']
populations = [126, 132, 96, 164, 328]

# load lists on Series, using cities as indexes and populations(Millions per city) as data
city_series = pd.Series(populations, index=cities)
print(city_series.index) # ['Detroit', 'Oklahoma', 'Nevada', 'Houston', 'New York'], dtype='object'


# Change the indexes of an existing Series
city_series.index = ['DT', 'OK', 'NV', 'HO', 'NY']
print(city_series.index) 
city_series.index = ['One', 'Two', 'Three', 'Four', 'Five']
print(city_series.index) 
city_series.index = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
print(city_series.index) 
city_series.index = ['A', 'B', 'C', 'D', 'E']
print(city_series.index) 
city_series.index = ['1', '2', '3', '4', '5']
print(city_series.index) 

# We can define any list of data as indexes for our Series
new_indexes = ['Hi', 'I', 'am', 'learning', 'pandas']
city_series.index = new_indexes
print(city_series.index)
print(city_series)

"""Second Example"""
data = ['Diana', 'Joseph', 'Fernando', 'Erika', 'Andrew']
indexes = ['A', 'B', 'C', 'D', 'E']

person_series = pd.Series(data, index=indexes)
print(person_series)
person_series.index = ['TAG1001', 'TAG1002', 'TAG1003', 'TAG1004', 'TAG1005']
print(person_series)
print(person_series.index)