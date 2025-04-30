import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3

# Load dataset
df = pd.read_excel('./DataSets/people_data.ods')

# Rename a column 'Ocupation' to 'Occupation'
df.rename(columns={'Ocupation':'Occupation'}, inplace=True)

# Load fixed dataset
df.to_excel('./DataSets/people_data.xlsx')
df = pd.read_excel('./DataSets/people_data.xlsx')

# Save Excel as CSV
df.to_csv('./DataSets/people_data.csv', index=False)

# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Write dataframe as DB table
df.to_sql("Population", conn, index=False, if_exists="replace")

def show_oldest_people(execute:bool=False) -> None:
    if execute:
        # Fetch oldest people
        query = "SELECT * FROM Population WHERE age > 60"
        result = pd.read_sql_query(query, conn)
        print(result)


def show_salary_sum_by_name(execute:bool=False) -> None:
    if execute:
        """ Get salary sumation grouped by name and visualizing it in a seaborn plot """
        query = """
            SELECT name AS Name, COUNT(*) AS NamesCount, SUM(salary) AS TotalSalary
            FROM Population
            WHERE name NOT NULL AND salary NOT NULL
            GROUP BY name
            ORDER BY name ASC
            LIMIT 10;
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

def show_average_salary_by_occupation(execute:bool=False) -> None:
    if execute:
        """ Get avg salary grouped by occupation showing only the first 10 placed in descending order """
        query = """
            SELECT occupation AS Occupation, AVG(salary) AS AverageSalary
            FROM Population
            GROUP BY occupation
            ORDER BY AverageSalary DESC
            LIMIT 10;
        """
        queryset_df = pd.read_sql_query(query, conn)
        # Create a figure with multiple subplots
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2x2 grid of plots

        sns.barplot(x='Occupation', y='AverageSalary', data=queryset_df, ax=axes[0, 0])
        axes[0, 0].set_title("Bar Plot")
        axes[0, 0].tick_params(axis='x', rotation=85)
        sns.boxplot(x='Occupation', y='AverageSalary', data=queryset_df, ax=axes[0, 1])
        axes[0, 1].set_title("Box Plot")
        axes[0, 1].tick_params(axis='x', rotation=85)
        sns.violinplot(x='Occupation', y='AverageSalary', data=queryset_df, ax=axes[1, 0])
        axes[1, 0].set_title("Violin Plot")
        axes[1, 0].tick_params(axis='x', rotation=85)
        sns.pointplot(x='Occupation', y='AverageSalary', data=queryset_df, ax=axes[1, 1])
        axes[1, 1].set_title("Point Plot")
        axes[1, 1].tick_params(axis='x', rotation=85)

        # Adjust layout to prevent overlap
        plt.tight_layout()

        # Show the chart
        plt.show() # We discovered a carpenter earns more than a programmer in average, even postmen earn more than a firefighter, why? I don´t know, maybe, what we should do is reduce salary for carpenters and postmen


def show_government_support_by_cities_over_occupations(execute:bool=False) -> None:
    if execute:
        """ Find cities where government is paying more for support to citizens """
        query = """
            SELECT City, Occupation, SUM(SupportAmount) AS SumSupportAmount
            FROM Population
            WHERE Name IS NOT NULL OR Salary IS NOT NULL
            GROUP BY City, Occupation;
        """

        queryset = pd.read_sql_query(query, conn)
        print(queryset)

        # Heatmap
        pivot_table = queryset.pivot(index='City', columns='Occupation', values='SumSupportAmount')
        pivot_table.fillna(0, inplace=True) # Replace NaN with 0 for the heatmap
        plt.figure(figsize=(14, 8))
        sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='magma')
        plt.title('Government Support by CIty and Occupation')
        plt.tight_layout()  # Prevent clipping
        plt.show()
    pass

def show_support_amount_and_salary_relation_by_occupation(execute:bool=False):
    if execute:
        query = """
            SELECT Occupation, SUM(salary) AS sum_salary, AVG(salary) AS avg_salary, SUM(SupportAmount) AS sum_support_amount
            FROM Population
            WHERE name IS NOT NULL AND salary IS NOT NULL
            GROUP BY Occupation
            ORDER BY SupportAmount DESC;
        """
        queryset = pd.read_sql_query(query, conn)
        print(queryset)

        # Remove None values from occupations
        queryset = queryset[queryset['Occupation'] != 'None']
        print(queryset)

        # Set Occupation as index
        queryset.set_index('Occupation', inplace=True)

        # Sort by avg_salary desc
        queryset.sort_values(by='avg_salary', ascending=False, inplace=True)

        # Plot comparative bar chart
        plt.style.use('dark_background')
        queryset[['sum_salary', 'avg_salary', 'sum_support_amount']].plot(
            kind='line',
            figsize=(12, 6),
            color=['royalblue', 'purple', 'violet']
        )
        plt.title('Total Salary vs. Government Support by Occupation')
        plt.xlabel('Occupation')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.legend(['Total Salary', 'Average Salary', 'Government Support'])
        plt.tight_layout()
        plt.grid(False)
        plt.show()

show_government_support_by_cities_over_occupations(False)
show_support_amount_and_salary_relation_by_occupation(True)