import sqlite3
import pandas as pd

conn = sqlite3.connect('ecom.db')

query = """
SELECT 
    c.name AS customer_name,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    (oi.quantity * p.price) AS total_price
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
ORDER BY o.order_date DESC;
"""

df = pd.read_sql_query(query, conn)
print(df.head())

conn.close()
