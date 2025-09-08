import pandas as pd
import sqlite3



# ---------------- DB SETUP ----------------
try:
    with sqlite3.connect("../db/lesson.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY,
                    product_name TEXT UNIQUE NOT NULL,
                    price REAL NOT NULL)
                    """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS line_items (
                    line_item_id INTEGER PRIMARY KEY,
                    quantity INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)

        
                    
      
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# ---------------- ADD FUNCTIONS ----------------
def add_products(cursor, product_id, product_name, price):
    try:
        cursor.execute("INSERT INTO products (product_id, product_name, price) VALUES (?,?,?)", (product_id, product_name, price))
    except sqlite3.IntegrityError:
        print(f"{product_name} is already in the database.")

def add_line_items(cursor, line_item_id, quantity, product_id):
    try:
        cursor.execute("INSERT INTO line_items (line_item_id, quantity, product_id) VALUES (?,?,?)", (line_item_id, quantity, product_id))
    except sqlite3.IntegrityError:
        print(f"{line_item_id} is already in the database.")








with sqlite3.connect("../db/lesson.db") as conn:
    cursor = conn.cursor()

# ---------------- DATA ----------------

    add_products(cursor, 1, 'milk', 3.99)
    add_products(cursor, 2, 'eggs', 2.99)
    add_products(cursor, 3, 'coffee', 4.65)
    add_products(cursor, 4, 'rice', 1.99)

    add_line_items(cursor, 1, 1, 1)
    add_line_items(cursor, 2, 2, 2)
    add_line_items(cursor, 3, 1, 3)
    add_line_items(cursor, 4, 1, 4)




    conn.commit()







sql_statement = """
        SELECT line_items.line_item_id, line_items.quantity, products.product_id, products.product_name, products.price
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        """

#-------------- Read into dataframe --------------
df = pd.read_sql_query(sql_statement, conn)

print(df)

df['total'] = df['quantity'] * df['price']
print(df.head(5))