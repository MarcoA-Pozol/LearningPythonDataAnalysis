import pandas as pd
import matplotlib.pyplot as plt

# Load dataframe from csv file
df = pd.read_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')
print(df)

"""Number of people per gender"""
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

"""Number of people per city"""
# Count the number of rows per city
city_counts = df['City'].value_counts()
print(city_counts)

# Visualizing city_counts in a Bar plot
plt.figure(figsize=(6, 4))
bars = plt.bar(city_counts.index, city_counts.values, color=['red', 'green', 'blue', 'yellow', 'pink', 'purple', 'orange', 'brown', 'gold', 'royalblue'])
plt.xlabel('City')
plt.ylabel('Population')
plt.title('Cities Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(height),
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )
plt.xticks(rotation=65)
plt.show()