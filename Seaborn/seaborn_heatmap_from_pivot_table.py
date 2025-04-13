import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')
names_per_city_counts = df.pivot_table(index='Name', columns='City', aggfunc='size', fill_value=0)
print(names_per_city_counts)

# Heatmap of pivot table
plt.figure(figsize=(14, 8))
sns.heatmap(
    names_per_city_counts,
    annot=True,           # Show the count numbers in each cell
    fmt='d',              # Format as integers
    cmap='YlGnBu',        # Color palette 
    linewidths=0.5,       # Lines between cells
    cbar_kws={'label': 'Name Count'}  # Colorbar label
)

plt.title('Number of People per Name in Each City', fontsize=16)
plt.xlabel('City')
plt.ylabel('Name')
plt.xticks(rotation=45, ha='right')  # Rotate city labels for readability
plt.tight_layout()
plt.show()