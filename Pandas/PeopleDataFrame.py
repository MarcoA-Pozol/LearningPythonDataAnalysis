import pandas as pd
import random

# Create the dataframe
df = pd.read_csv(filepath_or_buffer="LearningPythonDataAnalysis/DataSets/people_data.csv")
print(df)


# Elder (>=60) female people from Los Angeles received help from the goverment, identify them
elder_female_people_from_los_angeles = df[(df['Age']>=60) & (df['Gender']=='Female') & (df['City']=='Los Angeles')]
print(elder_female_people_from_los_angeles)

# Identify young people under 21 years old
young_people_under_21 = df[df['Age']<21]
print(young_people_under_21)
# Locate whose have an score over 90, they are going to receive an in cash reward for their score
young_people_with_over_90_score = df[(df['Age']<21) & (df['Score']>90)]
print(young_people_with_over_90_score)
# Obtain the highest score of them to give him/her a notepad
print(young_people_with_over_90_score[young_people_with_over_90_score['Score'] == young_people_with_over_90_score['Score'].max()])
# As we can see, we can re-filter the previous filtered df

# Obtain the oldest person 
print(df.loc[df['Age'].idxmax()])
# Obtain the youngest person
print(df.loc[df['Age'].idxmin()])

# Find the most common city of people under 25 years old
people_under_25 = df[df['Age']<25]
print(people_under_25)
most_common_city = people_under_25['City'].value_counts().idxmax()
print(f'Most Common City: {most_common_city}')

# Filter the most common name in male and female people
male_people = df[df['Gender']=='Male']
female_people = df[df['Gender']=='Female']
most_common_male_name = male_people['Name'].value_counts().idxmax()
most_common_female_name = female_people['Name'].value_counts().idxmax()
print(f'Most common male name: {most_common_male_name} - {male_people[male_people["Name"]==most_common_male_name].value_counts()}')
print(f'Most common female name: {most_common_female_name} - {female_people[female_people["Name"]==most_common_female_name].value_counts()}')

# Add a new column with rows of data for every user (Ocupation)
ocupations_options = [
    "Police Officer", "Firefigther", "Medic", "Postman", "Windows Cleaner", "Store Asistant", "Programer", "Architect", "Construction Worker", "Housekeeper", "Food Deliver", "Business Man", "Secretary", "Financial Manager","Enterprises Manager", "Plumber", "Carpenter", "Nurse", "Babysiter", "Fit Trainer", "Periodist", "Youtuber", "Bartender"
]
ocupations = []
for _ in range(0, 100+1):
    random_ocupation = random.choice(ocupations_options)
    ocupations.append(random_ocupation)
ocupations_series = pd.Series(ocupations, name='Ocupation')

if ocupations_series.name not in df.columns:
    df[ocupations_series.name] = ocupations_series
    print("New column 'Ocupation' created succesfully!")
else:
    print("Column 'Ocupation' already exists.")
print(df)

# Save the new updated dataframe
df.to_csv("LearningPythonDataAnalysis/DataSets/people_data.csv", index=False)

# Identify nurses
nurses = df[df['Ocupation']=='Nurse']
print(nurses)

# Change name of Nuse with ID 7 to a female name
nurses.loc[nurses['ID'] == 7, 'Name'] = 'Helen'
print(nurses)

# Adding a column for salary
salaries = []
for _ in range(0, 100+1):
    salary = random.randint(800, 8000)
    salaries.append(salary)
salaries_serie = pd.Series(salaries)
df['Salary'] = salaries_serie

"""Adding new rows"""
# Data Options
name_options = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Sophia", "James", "Isabella", "Benjamin", "Mia", "Ethan", "Charlotte", "Lucas", "Amelia", "Mason", "Harper", "Logan", "Ella", "Alexander", "Grace","Henry", "Lily", "Daniel", "Scarlett", "Michael", "Zoe"]
gender_options =  ['Male', 'Female', 'Other']
city_options = ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "San Francisco", "Seattle", "Dallas", "Atlanta", "Boston", "Denver", "Phoenix", "Las Vegas", "San Diego", "Philadelphia", "Austin", "Orlando", "Washington D.C.", "Nashville", "Detroit", "Minneapolis", "Portland", "Charlotte", "Indianapolis", "San Antonio", "Tampa"]
ocupations_options = ocupations_options

# Including 50 new records
new_people = []
for _ in range(0, 50+1):
    person = pd.DataFrame([{
        'Name': random.choice(name_options),
        'Age': random.randint(0, 120),
        'Gender': random.choice(gender_options),
        'City': random.choice(city_options),
        'Score': random.uniform(20, 120),
        'Ocupation': random.choice(ocupations_options),
        'Salary': random.randint(800, 8000),
    }])
    df = pd.concat([df, person], ignore_index=True)

# Drop uneccesary 'Occupation' column and save the updated file
df.drop(columns=['Occupation'], inplace=True)
df.to_csv("LearningPythonDataAnalysis/DataSets/people_data.csv", index=False)
print(df)