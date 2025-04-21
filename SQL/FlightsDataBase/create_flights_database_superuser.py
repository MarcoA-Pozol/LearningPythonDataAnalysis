import psycopg2
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Set client_encoding to UTF-8
os.environ['PGCLIENTENCODING'] = 'UTF8'

try:
    # Connect to default database to create a new superuser for FlightsDB
    conn = psycopg2.connect(
        dbname='postgres',
        user=os.getenv('DEFAULT_DB_USER'),
        password=os.getenv('DEFAULT_DB_PASSWORD'),
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    print('Connected to default database!')
except Exception as e:
    print(f'Connection to default postgres database is refused: {e}')

try:
    # Create new superuser for FlightsDB
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    cursor.execute('CREATE USER "%s" WITH PASSWORD %s;', (db_user, db_password))
    print('New user was created!')
except Exception as e:
    print(f'Error during creating a new superuser: {e}')

try:
    # Connect to FlightsDB
    conn = psycopg2.connect(
        dbname='FlightsDB',
        user=db_user,
        password=db_password,
        host='localhost',
        port='5432'
    )
    print('Connected to FlightsDB!')
except Exception as e:
    print(f'Connection to FlightsDB was refused: {e}')

try:
    # Grant superuser privileges to new user for FlightsDB
    # cursor.execute(f'ALTER USER {db_user} WITH SUPERUSER;')
    cursor = conn.cursor()
    cursor.execute(f'GRANT ALL PRIVILEGES ON DATABASE FlightsDB TO {db_user};')
    # Verify user creation
    print(cursor.execute('SELECT username, usesuper FROM pg_user;'))
except Exception as e:
    print(f'Error during granting superuser privileges to the new created user: {e}')
finally:
    cursor.close()
    conn.close()