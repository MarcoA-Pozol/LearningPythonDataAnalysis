import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('LearningPythonDataAnalysis/DataSets/people_data.csv')
ocupations_per_gender_counts = df.pivot_table(index='Ocupation', columns='Gender', aggfunc='size', fill_value=0)

# Heatmap of pivot table
plt.figure(figsize=(14, 8))
sns.heatmap(
    ocupations_per_gender_counts,
    annot=True,           # Show the count numbers in each cell
    fmt='d',              # Format as integers
    cmap='magma',        # Color palette (coolwarm, magma, viridis)
    linewidths=0.5,       # Lines between cells
    cbar_kws={'label': 'Ocupations Count'}  # Colorbar label
)

plt.title("Ocupations count per gender", fontsize=16)
plt.xlabel('Gender')
plt.ylabel('Ocupation')
plt.xticks(rotation=45, ha='right')  # Rotate city labels for readability
plt.tight_layout()
plt.show()