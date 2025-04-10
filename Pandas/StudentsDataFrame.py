import pandas as pd

# Create the dataframe
df = pd.read_csv(filepath_or_buffer="LearningPythonDataAnalysis/DataSets/users_data.csv")
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