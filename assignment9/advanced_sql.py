import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    cursor = conn.cursor()

# ---------------------------Task 1------------------------------
total_price =  """ 
    SELECT o.order_id, li.quantity, p.price, p.price * li.quantity AS line_total
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON p.product_id = li.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id ASC
    LIMIT 5;
    """
    


    # Return total price using AS total_price and customer_id AS customer_id_b. Return customer_id and total_price in subquery. Main statement, left join the customer table with the results of the subquery, using ON customer_id = customer_id_b
#------------------------------Task2-------------------------------
average_price = """
SELECT
  c.customer_name,
  AVG(t.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (
  SELECT
    o.order_id,
    o.customer_id AS customer_id_b,
    SUM(li.quantity * p.price) AS total_price
  FROM orders AS o
  JOIN line_items AS li ON li.order_id = o.order_id
  JOIN products  AS p  ON p.product_id = li.product_id
  GROUP BY o.order_id, o.customer_id
) AS t
  ON c.customer_id = t.customer_id_b
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id ASC
LIMIT 5;
"""

cursor.execute(total_price)
results = cursor.fetchall()
print(results)
conn.close()




#------------------------Task3-----------------------------

try:
    # Get customer_id
    cursor.execute("SELECT customer_id FROM customers WHERE name = 'Perez and Sons';")
    customer_id = cursor.fetchone()[0]

    # Get employee_id
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
    employee_id = cursor.fetchone()[0]

    # Get 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
    product_ids = [row[0] for row in cursor.fetchall()]

    # Begin transaction
    conn.execute("BEGIN;")

    # Insert into orders, return order_id
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id;
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # Insert line_items (10 of each product)
    for pid in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?);
        """, (order_id, pid, 10))

    # Commit transaction
    conn.commit()

    # Print the new line items
    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.name
        FROM line_items AS li
        JOIN products AS p ON li.product_id = p.product_id
        WHERE li.order_id = ?;
    """, (order_id,))
    for row in cursor.fetchall():
        print(row)  # (line_item_id, quantity, product_name)

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)








#------------------------TASK4-----------------------------
print("\nTask 4: Employees with more than 5 orders")
task4_query = """
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5;
"""
cursor.execute(task4_query)
for row in cursor.fetchall():
    print(row)  # (employee_id, first_name, last_name, order_count)


# Close 
conn.close()