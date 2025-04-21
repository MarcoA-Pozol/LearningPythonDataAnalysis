import psycopg2
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

try:
    # Connect to default postgres database to create a new one
    conn = psycopg2.connect(
        dbname="postgres",
        user=os.getenv("DEFAULT_DB_USER"),
        password=os.getenv("DEFAULT_DB_PASSWORD"),
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    print('Succesfully connected to postgres database!')
except Exception as e:
    print(f'Error during connecting to default postgres database: {e}')

try:
    # Create FlightsDB
    db_name = "FlightsDB"
    cursor.execute(f'CREATE DATABASE {db_name};')
    print('New database with name {} was succesfully created!'.format(db_name,))
except Exception as e:
    print(f'Error during creating a new database with name {db_name}: {e}')
finally:
    cursor.close()
    conn.close()