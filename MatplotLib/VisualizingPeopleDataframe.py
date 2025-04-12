import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm # Colormap
from matplotlib.patches import Patch # Legends

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
city_counts = df['City'].value_counts(sort=False) # Sort for unordered list
print(city_counts)

# Visualizing city_counts in a Bar plot
plt.figure(figsize=(6, 4))
bars = plt.bar(city_counts.index, city_counts.values, color=['royalblue'], edgecolor='black')
user_city = input('Select a City: [New York, Phoenix, Houston, Los Angeles, Chicago, Indianapolis, Austin, Charlotte, Detroit, Las Vegas, Minneapolis, San Francisco, Atlanta, Philadelphia, Miami, Nashville, Tampa, Denver, Seattle, Orlando, Boston, San Diego, Portland, San Antonio, Dallas, Washington D.C.]') # Get city of the user
selected_idx = list(city_counts.index).index(user_city) # Get index of the user's city selection
max_idx = city_counts.values.argmax() # Get index of city with more population than others
min_idx = city_counts.values.argmin() # Get index of city with lesser population than others
bars[selected_idx].set_color('green') # Use green color for selected by user city
bars[max_idx].set_color('red')
bars[min_idx].set_color('gray')
# Custom Legends
legend_elements = [
    Patch(facecolor='royalblue', label='Cities'),
    Patch(facecolor='green', label="User's selection"),
    Patch(facecolor='red', label='Overpopulated'),
    Patch(facecolor='gray', label='Underpopulated'),
]
plt.legend(handles=legend_elements)
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

"""People per Ocupation"""
# Count the number of rows per ocupation
ocupation_counts = df['Ocupation'].value_counts()
print(ocupation_counts)

# Colormap for bars
colors = cm.Set3(range(len(ocupation_counts)))

# Visualizing ocupation_counts in a Bar plot
plt.figure(figsize=(6, 4))
bars = plt.bar(ocupation_counts.index, ocupation_counts.values, color=colors, edgecolor='royalblue')
plt.xlabel('Ocupation')
plt.ylabel('People')
plt.title('People Ocupations')
plt.grid(axis='y', linestyle='dashdot', alpha=0.7)
plt.gca().set_axisbelow(False) # Howizontal grid lines behind/infront bars
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