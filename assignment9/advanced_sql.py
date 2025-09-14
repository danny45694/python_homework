import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    cursor = conn.cursor()

# Task 1---------------------------------------------------------------
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



