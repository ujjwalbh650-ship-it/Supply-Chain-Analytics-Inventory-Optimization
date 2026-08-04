# 📦 Supply Chain Analytics & Inventory Optimization

> End-to-End Supply Chain Analytics Pipeline using Python, SQL, DuckDB, and Power BI



---

# 📌 Project Overview

This project demonstrates an end-to-end Supply Chain Analytics workflow, starting from raw operational data and transforming it into business-ready analytical datasets using a modern Medallion Architecture (Bronze → Silver → Gold).

The transformed data is then modeled into a Star Schema and visualized through interactive Power BI dashboards to support inventory planning, sales monitoring, stock movement analysis, and supply chain decision-making.

---

# 🎯 Business Problem

Supply chain teams receive data from multiple operational systems such as:

- Sales Transactions
- Inventory Snapshots
- Product Master
- Location Master
- Inventory Movements

These datasets are often inconsistent, contain formatting issues, and are not directly suitable for analytics.

This project builds an automated analytics pipeline that:

- Cleans raw operational data
- Standardizes business fields
- Creates analytical fact and dimension tables
- Generates KPIs for inventory and sales performance
- Enables interactive Power BI dashboards

---

# 🏗 Project Architecture

`# 🏗 Project Architecture

The project follows a Medallion Architecture (Bronze → Silver → Gold) to transform raw operational data into analytics-ready datasets for reporting and decision-making.

<p align="center">
  <img src="images/architecture.png" alt="Supply Chain Analytics Architecture" width="950"/>
</p>
---

# 📂 Project Structure

```
Supply_Chain_Analytics/

│
├── data/
│
├── sql/
│   │
│   ├── bronze/
│   │      bronze_product_master.py
│   │      bronze_sales_transaction.py
│   │      bronze_location_master.py
│   │      bronze_inventory_snapshot.py
│   │      bronze_inventory_movements.py
│   │
│   ├── silver/
│   │      silver_product_master.py
│   │      silver_sales_transaction.py
│   │      silver_location_master.py
│   │      silver_inventory_snapshot.py
│   │      silver_inventory_movements.py
│   │
│   └── gold/
│          gold_dim_product.py
│          gold_dim_location.py
│          gold_fact_sales.py
│          gold_fact_inventory_snapshot.py
│          gold_fact_inventory_movements.py
│          gold_adv_fact_inventory_exposure.py
│
├── dashboard/
│      SupplyChainDashboard.pbix
│
└── README.md
```

---

# 🥉 Bronze Layer

Purpose:

Store raw operational data without modification.

Tables

- Product Master
- Sales Transactions
- Inventory Snapshots
- Inventory Movements
- Location Master

Characteristics

✔ Raw Data

✔ No Cleaning

✔ Source Copy

---

# 🥈 Silver Layer

Purpose

Clean and standardize operational data.

Data transformations include

- Trim spaces
- Uppercase text
- Standardize Date Formats
- Data Type Conversion
- Remove formatting inconsistencies
- Null handling

Output

Clean business-ready tables.

---

# 🥇 Gold Layer

Purpose

Create analytics-ready data model.

### Dimension Tables

| Table | Purpose |
|---------|----------|
| Dim Product | Product Information |
| Dim Location | Store / Warehouse Information |

### Fact Tables

| Table | Purpose |
|---------|----------|
| Fact Sales | Sales Transactions |
| Fact Inventory Snapshot | Daily Inventory |
| Fact Inventory Movements | Stock Movements |
| Advanced Fact Inventory Exposure | Weekly Inventory Exposure |

---

# ⭐ Star Schema

```text
               Dim Product
                     │
                     │
                     │
Dim Location ───── Fact Sales ───── Dim Date
                     │
                     │
      Fact Inventory Snapshot
                     │
                     │
      Fact Inventory Movements
                     │
                     │
 Advanced Inventory Exposure
```

---

# 📊 Advanced Inventory Exposure Table

One of the key analytical tables in this project.

It combines:

✔ Weekly Sales

✔ Weekly Inventory

✔ Weekly Stock Movements

into a single business table.

Granularity

```
WeekStartDate
LocationID
ProductSKU
```

Metrics

- Weekly Sales Quantity
- Week End Inventory
- Net Movement Quantity

Business Benefit

Allows supply chain teams to identify

- Low stock situations
- Overstock
- Inventory exposure
- Replenishment opportunities

---

# 📈 Power BI Dashboards

### Executive Dashboard

Provides high-level business KPIs

- Total Sales
- Units Sold
- Week End Inventory
- Net Movement
- Low Stock %

---

### Inventory Analytics

Tracks

- Inventory Trends
- Stock Availability
- Product Coverage
- Inventory Levels

---

### Movement Analytics

Analyzes

- Stock Inflow
- Stock Outflow
- Inventory Adjustments
- Warehouse Movements

---

# 🛠 Technologies Used

| Tool | Purpose |
|------|----------|
| Python | ETL Automation |
| SQL | Data Transformation |
| DuckDB | Analytical Database |
| DBeaver | Database Exploration |
| VS Code | Development |
| Power BI | Dashboard Development |

---

# 📌 Key Features

✔ Bronze → Silver → Gold ETL Pipeline

✔ Automated SQL execution using Python

✔ Data Cleaning & Standardization

✔ Star Schema Modeling

✔ Fact & Dimension Tables

✔ Inventory Exposure Analytics

✔ Interactive Power BI Dashboards

✔ Business KPI Reporting

---

# 📊 Business KPIs

- Total Sales
- Units Sold
- Weekly Sales
- Inventory On Hand
- Low Stock Percentage
- Inventory Movements
- Net Movement Quantity
- Product Availability

---

# 🚀 Future Improvements

- Incremental Data Loading
- Automated ETL Scheduling
- Supply Chain Forecasting
- Safety Stock Calculation
- Reorder Point Optimization
- Demand Forecasting
- ABC Inventory Classification

---

# 👨‍💻 Author

**Ujjwal Bhuyan**

Mechanical Engineering | Supply Chain Analytics | Data Analytics

Skills

- SQL
- Python
- Power BI
- DuckDB
- Data Modeling
- ETL Pipeline
- Supply Chain Analytics

---
