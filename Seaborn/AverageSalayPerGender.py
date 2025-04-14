import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd
import seaborn as sns

# Load dataset
df = pd.read_csv('../DataSets/people_data.csv')

# Get DataFrame of mean salary grouped by gender
gender_salary_average = df.groupby('Gender')['Salary'].mean().reset_index() # Convert this Series object to a DataFrame for its visualization in barplot
print(gender_salary_average)

# Barplot
plt.figure(figsize=(6, 4))
ax = sns.barplot(data=gender_salary_average, x='Gender', y='Salary', estimator='mean', palette=['blue', 'pink', 'purple'])

plt.title('Average Salary per Gender')
plt.xlabel('Gender')
plt.ylabel('Salary (USD per month)')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Custom Legends
legend_elements = [
    Patch(facecolor='blue', label='Male'),
    Patch(facecolor='pink', label="Female"),
    Patch(facecolor='purple', label='Other'),
]

# Add values on top of bars
for i in ax.containers:
    ax.bar_label(i, fmt='%.2f', fontsize=10, weight='bold')

plt.legend(handles=legend_elements)
plt.tight_layout()
plt.show()