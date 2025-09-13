import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    cursor = conn.cursor()

# Join the tables
total_price =  """ WITH 
    join_tables AS (
    SELECT orders, products, line_items
    FROM orders
    JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON products.product_id = line_items.product_id
    GROUP BY order_id
),
    add_tables AS (
    SELECT order_id, SUM(products.price * line_items.quantity)
    FROM joined_tables
    ORDER BY order_id
    LIMIT 5
    )
    """

cursor.execute(total_price)
results = cursor.fetchall()
print(results)
conn.close()
