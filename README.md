# E-Commerce Sales Analytics

## Project Overview

This project analyzes e-commerce sales data to identify sales trends, regional performance, product performance, customer segment contribution, profitability, and order-status patterns.

The project demonstrates an end-to-end basic data analytics workflow using Python, Pandas, SQL, and Tableau.

## Tools & Technologies

- Python
- Pandas
- SQL
- SQLite
- Tableau
- CSV

## Dataset

The dataset contains **5,000 synthetic e-commerce order records** created for analytics practice and portfolio demonstration.

Key fields include:

- Order Date
- Customer
- Region
- Product
- Category
- Quantity
- Sales
- Discount
- Profit
- Shipping Days
- Order Status

## Data Analysis

### Python & Pandas
- Loaded and inspected the raw dataset
- Checked missing values and duplicates
- Validated numerical fields
- Created profit margin and date-based fields
- Performed exploratory data analysis
- Generated analytical charts

### SQL
SQL was used to analyze:

- Overall sales and profit
- Monthly sales and profit
- Regional performance
- Category profitability
- Top-performing products
- Customer segment performance
- Discount vs. profit
- Order-status performance

### Tableau Dashboard

The final dashboard includes:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Monthly Sales Trend
- Sales by Region
- Profit by Category
- Top 10 Products by Sales
- Customer Segment Analysis
- Order Status Analysis

## Key KPIs

| KPI | Value |
|---|---:|
| Total Sales | ₹76,227,596 |
| Total Profit | ₹10,779,298 |
| Total Orders | 5,000 |
| Total Customers | 1,161 |

## Project Structure

```text
ecommerce-sales-analytics/
├── README.md
├── data/
│   └── ecommerce_orders_cleaned.csv
├── python/
│   └── analysis.py
├── sql/
│   └── sql_analysis.py
└── charts/
    ├── monthly_sales.png
    ├── sales_by_category.png
    └── sales_by_region.png
```

## Business Objective

The objective is to transform raw e-commerce order data into meaningful business insights that can support decisions related to sales performance, product strategy, customer segments, regional performance, and profitability.

## Note

This project uses synthetic data and was created for learning, analytics practice, and portfolio demonstration.
