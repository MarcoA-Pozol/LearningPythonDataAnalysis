import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3

# Load dataset
df = pd.read_excel('./DataSets/people_data.ods')
print(df)

# Save Excel as CSV
df.to_csv('./DataSets/people_data.csv')

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

# Create a bar chart for salary summation by name
sns.barplot(x='Name', y='TotalSalary', data=queryset_df)

# Customize the plot
plt.title("Salary Summation by Name")
plt.xlabel("Name")
plt.ylabel("Total Salary")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the chart
plt.show()
