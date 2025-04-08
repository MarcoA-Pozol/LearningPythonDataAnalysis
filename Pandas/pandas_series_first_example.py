import pandas as pd

"""First Steps"""
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



"""Multiple series to DataFrame"""
# Create a table type XLSX with students data
# Create a custom indexes list
indexes = ['A', 'B', 'C', 'D']
# Create series for each dataset
first_names = pd.Series(['Roger', 'Hanna', 'Gabriel', 'Jazmin'], name='FirstName', index=indexes)
last_names = pd.Series(['Ferdinand', 'Larosse', 'Garcia', 'Otto'], name='LastName', index=indexes)
ages = pd.Series([26, 32, 35, 29], name='Age', index=indexes)
courses = pd.Series(['Machine Learning II', 'Communication and Expression III', 'Software Engineering I', 'Excel IV'], name='Course', index=indexes)
# Once Series with data are created, the next step is to create the DataFrame
students_dataframe = pd.DataFrame(data={'FirstName':first_names, 'LastName':last_names, 'Age':ages, 'Course':courses}, index=indexes)
# Add a title to the DataFrame
students_dataframe.title = "Students's Current Courses"
# Visualize dataframe in console
print(f'\n{students_dataframe}')
print(f'Dataset title: {students_dataframe.title}')


"""Second Example of DataFrame composed of Series without custom indexes"""
# Create series with data
animals = pd.Series(['Python', 'Cat', 'Lion', 'Eagle', 'Dog', 'Shark'], name='Animals')
food = pd.Series(['Mouse', 'Fish', 'Zebra', 'Snake', 'Meat', 'Meat'], name='food')
location = pd.Series(['Savanna', 'House', 'Savanna', 'Sky', 'House', 'Sea']) # Name is not strictly neccesary to be defined, it´s only for Series, not for the composed DataFrame
print(animals)
# Composes a DataFrame with series
animals_dataframe = pd.DataFrame({'Animal':animals, 'Food':food, 'Location':location})
# Visualize dataframe
animals_dataframe.title = 'Animals'
print(f'\n{animals_dataframe}')
print(f'Dataset title: {animals_dataframe.title}') # Easy config for a simple DataFrame composed of many Series from Pandas

# DataFrame of Users composed of 4 Series
usernames = pd.Series(['Dewey99', 'Nixon405', 'Lili_70', 'DestroyerM', 'TheGamer', 'JuanVillalvazo', 'JasonJ', 'HalseyW'])
emails = pd.Series(['dewey99@gmail.com', 'nixon405@gmail.com', 'lili_70@gmail.com', 'destroyerm@gmail.com', 'thegamer@gmail.com', 'juanvillalvazo@gmail.com', 'jasonj@gmail.com', 'halseyw@gmail.com'])
ages = pd.Series([32, 29, 26, 19, 45, 35, 19, 24])
countries = pd.Series(['USA', 'UK', 'Peru', 'Mexico', 'Alemania', 'Mexico', 'USA', 'USA'])
print(usernames, emails, ages, countries)
# Create DataFrame composed with multiple series
users_dataframe = pd.DataFrame({'Username': usernames, 'Email': emails, 'Age': ages, 'Country': countries})
users_dataframe.title = 'Usernames data'
print(f'\n{users_dataframe}')
print(f'Dataset title: {users_dataframe.title}')

# DataFrame Exploration and Manipulation
print(users_dataframe.head()) # Retrieves all dataframe
print(users_dataframe.info()) # Retrieves columns info(headers, fields, number of entries, dtype)
print(users_dataframe.tail()) # Retrieves all dataframe
print(users_dataframe.describe(include='all')) # Retrieves count, unique, top, freq, mean, std, min, 25, 50, 75, max for each dataset column
print(users_dataframe.columns) # Retrieves the list of colums of the dataframe
print(users_dataframe.shape) # Returns number of rows and number of columns of the dataframe
print(users_dataframe.index) # Returns the indexes range of the dataframe, number of rows including the header
print(users_dataframe.dtypes) # Retrieves the columns of the dataframe with its types of data