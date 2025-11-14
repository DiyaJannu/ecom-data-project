# E-Commerce Data Project
This project generates synthetic e-commerce data, ingests it into SQLite, and runs SQL queries.
# Ecom Data Project

This project generates synthetic e-commerce data, ingests it into a SQLite database, and runs SQL queries to extract insights.

## 📁 Project Structure

<img width="774" height="471" alt="image" src="https://github.com/user-attachments/assets/0b083e9a-36fd-4547-b607-9651638fc721" />

## 🚀 How to Run

### 1. Generate Synthetic Data
```bash
python scripts/generate_data.py

## 🚀 How to Run

### 2. Ingest Data into SQLite
Loads the CSVs into a SQLite database (`ecom.db`).

```bash
python scripts/ingest_to_sqlite.py
### 3. to run query

python scripts/query_data.py

## 📊 Sample Output

```text
customer_name order_date product_name  quantity  total_price
0    John Doe   2023-11-01  Headphones         2       299.98
1  Jane Smith   2023-10-15      T-Shirt        1        19.99
2  Rahul Verma  2023-09-22        Book         3        45.00






