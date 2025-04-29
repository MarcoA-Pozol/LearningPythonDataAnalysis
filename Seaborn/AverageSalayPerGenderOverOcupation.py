import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd
import seaborn as sns

# Load dataset
df = pd.read_csv('./DataSets/people_data.csv')

# Get DataFrame of mean salary grouped by gender
gender_average_salary_over_ocupation = df.groupby(['Ocupation', 'Gender'])['Salary'].mean().reset_index() # Convert this Series object to a DataFrame for its visualization in barplot
print(gender_average_salary_over_ocupation)

# Barplot
plt.figure(figsize=(6, 4))
ax = sns.barplot(data=gender_average_salary_over_ocupation, x='Ocupation', y='Salary', hue='Gender', estimator='mean', palette=['blue', 'pink', 'red']) # Use hue='Gender' to categorize the avg salary per ocupation per each gender 

plt.title('Average Salary per Gender Over Occupation')
plt.xlabel('Gender per Occupation')
plt.ylabel('Salary (USD per month)')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Custom Legends
legend_elements = [
    Patch(facecolor='blue', label='Male'),
    Patch(facecolor='pink', label="Female"),
    Patch(facecolor='red', label='Other'),
]
plt.legend(title='Gender')

# Add values on top of bars
for i in ax.containers:
    ax.bar_label(i, fmt='%.2f', fontsize=6)

plt.xticks(rotation=45, ha='right')
plt.legend(handles=legend_elements)
plt.tight_layout()
plt.show()