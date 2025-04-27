import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3

# Load dataset
df = pd.read_excel('./DataSets/people_data.ods')
print(df)

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
    SELECT name AS Name, COUNT(*) AS NamesCount, SUM(salary) AS PotentialSalary
    FROM Population
    GROUP BY name
    ORDER BY name ASC;
"""
queryset = pd.read_sql_query(query, conn)
print(queryset)