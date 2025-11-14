# E-Commerce Data Project
This project generates synthetic e-commerce data, ingests it into SQLite, and runs SQL queries.
# Ecom Data Project

This project generates synthetic e-commerce data, ingests it into a SQLite database, and runs SQL queries to extract insights.

## 📁 Project Structure

ecom-data-project/ ├── data/ # Generated CSV files ├── scripts/ # Python scripts │ ├── generate_data.py │ ├── ingest_to_sqlite.py │ └── query_data.py ├── ecom.db # SQLite database (created by script) ├── .gitignore └── README.md

## 🚀 How to Run

### 1. Generate Synthetic Data
```bash
python scripts/generate_data.py

### 2. Ingest Data into SQLite
```bash
python scripts/ingest_to_sqlite.py

### 3. Run SQL Query
```bash
python scripts/query_data.py

