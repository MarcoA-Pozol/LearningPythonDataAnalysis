import psycopg2
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

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

# Create FlightsDB
db_name = "FlightsDB"
cursor.execute(f'CREATE DATABASE {db_name};')

cursor.close()
conn.close()