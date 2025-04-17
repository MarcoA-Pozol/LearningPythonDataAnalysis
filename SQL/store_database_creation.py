import sqlite3

def create_database(database_name):
    """Create the database and its first table if they does not exists."""
    conn = sqlite3.connect(f'./DataBases/{database_name}.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname VARCHAR(100), lastname VARCHAR(100));""")
    conn.commit()
    cursor.close()
    conn.close()

create_database('TechStore')