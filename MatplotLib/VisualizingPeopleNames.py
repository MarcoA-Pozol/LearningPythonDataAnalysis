import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

# Loading the DataFrame from a CSV file
df = pd.read_csv('LearningPythonDataAnalysis/Datasets/people_data.csv')

# Create the plot
plt.figure(figsize=(6, 4))

# Obtaining bar´s data
name_counts = df['Name'].value_counts(sort=False)
bars = plt.bar(name_counts.index, name_counts.values, color='royalblue', edgecolor='blue')

# Identifying
max_idx = name_counts.values.argmax()
min_idx = name_counts.values.argmin()
bars[max_idx].set_color('green')
bars[min_idx].set_color('red')

# Custom Legends
legend_elements = [
    Patch(facecolor='royalblue', label='Names'),
    Patch(facecolor='green', label="Most used name"),
    Patch(facecolor='red', label='Least used name'),
]
plt.legend(handles=legend_elements)

# Counting in every bar top
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

# Customize the plot
plt.xlabel('Name')
plt.ylabel('Count')
plt.title('Names count in the USA')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=55)
plt.show()