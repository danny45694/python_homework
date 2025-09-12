import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    cursor = conn.cursor()

# Join the tables
    total_price = """
    SELECT orders, products, line_items
    FROM orders
    JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON products.product_id = line_items.product_id
    GROUP BY order_id
    SELECT order_id, SUM(products.price * line_items.quantity)
    ORDER BY order_id
    LIMIT 5
    """

    cursor.execute(total_price)
    results = cursor.fetchall()
    print(results)
    conn.close()


    2. Common Table Expressions (CTEs) with WITH clause:
CTEs define a temporary, named result set that can be referenced within a single SELECT, INSERT, UPDATE, or DELETE statement. This allows for defining a SELECT statement once and then reusing its result multiple times within the main query for clarity and modularity.
Code

WITH MyCTE AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition1
)
SELECT A.column1, B.column3
FROM MyCTE AS A
JOIN another_table AS B ON A.column2 = B.column2
WHERE A.column1 > (SELECT AVG(column1) FROM MyCTE);