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




#---------------------------------Task3-----------------------------

task3 = """
BEGIN;
PRAGMA foreign_keys = 1;

INSERT INTO orders (customer_id, employee_id, order_date)
VALUES (
  (SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'),
  (SELECT employee_id  FROM employees WHERE (first_name || ' ' || last_name) = 'Miranda Harris'),
  DATE('now')
)
RETURNING order_id;

INSERT INTO line_items (order_id, product_id, quantity)
SELECT
  (SELECT order_id FROM orders ORDER BY order_id DESC LIMIT 1),
  p.product_id,
  10
FROM products p
ORDER BY p.price ASC, p.product_id ASC
LIMIT 5;

COMMIT;

SELECT li.line_item_id, li.quantity, p.product_name
FROM line_items li
JOIN products p ON p.product_id = li.product_id
WHERE li.order_id = (SELECT order_id FROM orders ORDER BY order_id DESC LIMIT 1)
ORDER BY li.line_item_id;

"""






#-------------------------------TASK4------------------------------------

task4 = """
SELECT
  e.employee_id,
  e.first_name,
  e.last_name,
  COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders    AS o ON o.employee_id = e.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC, e.last_name, e.first_name;
"""