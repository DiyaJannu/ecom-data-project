import sqlite3
import pandas as pd

conn = sqlite3.connect('ecom.db')

# Load CSVs
customers = pd.read_csv('data/customers.csv')
products = pd.read_csv('data/products.csv')
orders = pd.read_csv('data/orders.csv')
order_items = pd.read_csv('data/order_items.csv')
reviews = pd.read_csv('data/reviews.csv')

# Save to DB
customers.to_sql('customers', conn, index=False, if_exists='replace')
products.to_sql('products', conn, index=False, if_exists='replace')
orders.to_sql('orders', conn, index=False, if_exists='replace')
order_items.to_sql('order_items', conn, index=False, if_exists='replace')
reviews.to_sql('reviews', conn, index=False, if_exists='replace')

conn.commit()
conn.close()
