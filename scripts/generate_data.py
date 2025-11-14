from faker import Faker
import pandas as pd
import random

fake = Faker()

# Customers
customers = pd.DataFrame([{
    'id': i,
    'name': fake.name(),
    'email': fake.email(),
    'signup_date': fake.date_between(start_date='-2y', end_date='today')
} for i in range(1, 201)])
customers.to_csv('data/customers.csv', index=False)

# Products
products = pd.DataFrame([{
    'id': i,
    'name': fake.word().capitalize(),
    'category': random.choice(['Electronics', 'Clothing', 'Books']),
    'price': round(random.uniform(10, 500), 2)
} for i in range(1, 101)])
products.to_csv('data/products.csv', index=False)

# Orders
orders = pd.DataFrame([{
    'id': i,
    'customer_id': random.randint(1, 200),
    'order_date': fake.date_between(start_date='-1y', end_date='today'),
    'total_amount': 0
} for i in range(1, 301)])
orders.to_csv('data/orders.csv', index=False)

# Order Items
order_items = []
for order in orders['id']:
    for _ in range(random.randint(1, 5)):
        pid = random.randint(1, 100)
        qty = random.randint(1, 3)
        order_items.append({
            'order_id': order,
            'product_id': pid,
            'quantity': qty
        })
order_items_df = pd.DataFrame(order_items)
order_items_df.to_csv('data/order_items.csv', index=False)

# Reviews
reviews = pd.DataFrame([{
    'product_id': random.randint(1, 100),
    'customer_id': random.randint(1, 200),
    'rating': random.randint(1, 5),
    'review_text': fake.sentence()
} for _ in range(500)])
reviews.to_csv('data/reviews.csv', index=False)
