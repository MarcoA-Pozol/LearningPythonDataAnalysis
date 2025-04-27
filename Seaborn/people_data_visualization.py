import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3

# Load dataset
df = pd.read_excel('./DataSets/people_data.ods')
print(df)

# Save Excel as CSV
# df.to_csv('./DataSets/people_data.csv', index=False)

# # Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Write dataframe as DB table
df.to_sql("Population", conn, index=False, if_exists="replace")

# Fetch oldest people
query = "SELECT * FROM Population WHERE age > 60"
result = pd.read_sql_query(query, conn)
print(result)

""" Get salary sumation grouped by name and visualizing it in a seaborn plot """
query = """
    SELECT name AS Name, COUNT(*) AS NamesCount, SUM(salary) AS TotalSalary
    FROM Population
    WHERE name NOT NULL AND salary NOT NULL
    GROUP BY name
    ORDER BY name ASC;
"""
queryset_df = pd.read_sql_query(query, conn)
print(queryset_df)

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2x2 grid of plots

sns.barplot(x='Name', y='TotalSalary', data=queryset_df, ax=axes[0, 0])
axes[0, 0].set_title("Bar Plot")
axes[0, 0].tick_params(axis='x', rotation=85)
sns.boxplot(x='Name', y='TotalSalary', data=queryset_df, ax=axes[0, 1])
axes[0, 1].set_title("Box Plot")
axes[0, 1].tick_params(axis='x', rotation=85)
sns.violinplot(x='Name', y='TotalSalary', data=queryset_df, ax=axes[1, 0])
axes[1, 0].set_title("Violin Plot")
axes[1, 0].tick_params(axis='x', rotation=85)
sns.pointplot(x='Name', y='TotalSalary', data=queryset_df, ax=axes[1, 1])
axes[1, 1].set_title("Point Plot")
axes[1, 1].tick_params(axis='x', rotation=85)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()
