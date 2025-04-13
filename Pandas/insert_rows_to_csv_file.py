import pandas as pd

# load dataset
df = pd.read_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')
print(df['Ocupation'].value_counts())

# Add rows to the dataframe
person1 = {'Name':'John', 'Age':28, 'Gender':'Male', 'City':'Oklahoma', 'Score':45250, 'Ocupation':'Dishwasher', 'Salary':980}
person2 = {'Name':'Carlos', 'Age':36, 'Gender':'Male', 'City':'New York', 'Score':21050, 'Ocupation':'Dishwasher', 'Salary':1150}
person3 = {'Name':'Tania', 'Age':21, 'Gender':'Male', 'City':'Detroit', 'Score':14550, 'Ocupation':'Dishwasher', 'Salary':860}

new_people = [person1, person2, person3]

for i in new_people:
    df.loc[len(df)] = i # Add new row on the last df row based on its len

# Comprobe we have new ocupations (Dishwasher)
print(df['Ocupation'].value_counts())
# Comprobe we have new names (Tania, Carlos, John)
print(df['Name'].value_counts())

# Save updated dataset
df.to_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')