import pandas as pd
import sqlite3

with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS line_items (
                   line_item_id INTEGER PRIMARY KEY,
                   quantity INTEGER,
        )   
    )"""
                
    sql_statement = """SELECT line_item_id, quantity, product_id, product_name, price
    
    
    
    """



try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") 
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                topic TEXT NOT NULL UNIQUE
            )
        """)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    df = pd.read_sql_query(sql_statement, conn)