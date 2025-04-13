import pandas as pd

# Load the dataset
df = pd.read_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')
names_per_city_counts = df.pivot_table(index='Name', columns='City', aggfunc='size', fill_value=0)
print(names_per_city_counts)

# Total number of people per city
print(names_per_city_counts.sum(axis=0)) # Axis 0 is 'X'
# Total numbe of people per name
print(names_per_city_counts.sum(axis=1)) # Axis 1 is 'Y'
# Who appears in the most cities?
print(names_per_city_counts.astype(bool).sum(axis=1).sort_values(ascending=False).head())
# Who appears in the least of cities?
print(names_per_city_counts.astype(bool).sum(axis=1).sort_values(ascending=True).head())
# Get cities list
print(df['City'].value_counts())


# Get data from Alice names
print(df[df['Name']=='Alice'].value_counts())
# Alice name is being sometimes related to a male gender, what is wrong, change it to female
try:
    df.loc[(df['Name'] == 'Alice') & (df['Gender'] == 'Male'), 'Gender'] = 'Female' # If Name is Alice and Gender is Male, change Gender to Female
    print(df[df['Name'] == 'Alice'][['Name', 'Gender']])
    df.to_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')
except:
    pass