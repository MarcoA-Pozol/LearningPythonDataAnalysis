import pandas as pd
import matplotlib.pyplot as plt

# Load dataframe from csv file
df = pd.read_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')
print(df)

# Count the number of rows per gender
gender_counts = df['Gender'].value_counts()

# Visualizing gender_counts in a Bar plot
plt.figure(figsize=(6, 4))
plt.bar(gender_counts.index, gender_counts.values, color=['lightblue', 'pink', 'yellow'])
plt.xlabel('Gender')
plt.ylabel('People')
plt.title('People per Gender')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()