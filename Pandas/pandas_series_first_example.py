import pandas as pd

# Defining normal lists
sizes_list = ['S', 'M', 'L', 'XL']
users_lists = ['Vandal', 'Ghost99X', 'ElectricWizzarddd', 'TheGamer']

# Transform python lists to pandas series object with a simple index
sizes_series = pd.Series(sizes_list)
users_series = pd.Series(users_lists)

# View results
print(sizes_series)
print(users_series)

# Creating a series object with custom indexes
indexes = ['a', 'b', 'c', 'd', 'e']
series_with_custom_index = pd.Series(['data1', 'data2', 'data3', 'data4', 'data5'],  indexes)
print(series_with_custom_index)

# We can assign custom indexes as keys, and insert values for each key(index)
indexes = ['A1', 'A2', 'A3', 'A4']
first_column = ['Marco', 'Pozol', 23, 'marcoantoniopozolnarciso@gmail.com']
users_series = pd.Series(first_column, indexes)
print(users_series)

# We can now see the format is similar of a table with the indexes on the left, and the columns on the following right side, then we can add more columns as if they were rows of a normal sql database table, but with the indexes vertically, then is is about columns, not rows,
second_column = ['Linda', 'Smith', 29, 'lindasmith@gmail.com']
third_column = ['Michail', 'Harshman', 42, 'michailharshman@gmail.com']
fourt_column = ['Denisse', 'Thompson', 36, 'denissethompson@gmail.com']

# Serializing lists into pandas series
first_series = pd.Series(first_column)
second_series = pd.Series(second_column)
third_series = pd.Series(third_column)
fourt_series = pd.Series(fourt_column)

# To vizualize it with the desired format as a table with indexes vertically and values instances displayed as columns we need a dataframe, the dataframe can be composed of series
users_dataframe = pd.DataFrame([first_series, second_series, third_series, fourt_series], indexes) # As we can see with this format, this has problems with visualization, when trying to show they ordered.
users_dataframe.title = "Users Data"
print(users_dataframe)

