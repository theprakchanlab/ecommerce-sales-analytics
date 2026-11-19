import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("ecommerce_orders.csv")

print("Dataset Shape:", df.shape)


# ==========================================
# 2. DATA CLEANING
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nUnique Values:")
print("Regions:", df["region"].unique())
print("Categories:", df["category"].unique())
print("Order Status:", df["order_status"].unique())

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Check negative values
print("\nNegative Values:")
print("Quantity:", (df["quantity"] < 0).sum())
print("Unit Price:", (df["unit_price"] < 0).sum())
print("Sales:", (df["sales"] < 0).sum())

# Remove duplicates
df = df.drop_duplicates()

# Create profit margin
df["profit_margin"] = np.where(
    df["sales"] != 0,
    (df["profit"] / df["sales"]) * 100,
    0
)

# Create time columns
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()

# Save cleaned data
df.to_csv("ecommerce_orders_cleaned.csv", index=False)

print("\nFinal Dataset Shape:", df.shape)
print("Cleaning completed successfully.")


# ==========================================
# 3. BUSINESS KPIs
# ==========================================

print("\n========== BUSINESS KPIs ==========")

total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
average_order_value = total_sales / total_orders

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))


# ==========================================
# 4. SALES BY REGION
# ==========================================

print("\n========== SALES BY REGION ==========")

region_sales = (
    df.groupby("region")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print(region_sales)


# ==========================================
# 5. SALES BY CATEGORY
# ==========================================

print("\n========== SALES BY CATEGORY ==========")

category_sales = (
    df.groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)


# ==========================================
# 6. PROFIT BY CATEGORY
# ==========================================

print("\n========== PROFIT BY CATEGORY ==========")

category_profit = (
    df.groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)

print(category_profit)


# ==========================================
# 7. TOP 10 PRODUCTS
# ==========================================

print("\n========== TOP 10 PRODUCTS ==========")

top_products = (
    df.groupby("product_name")
    .agg(
        sales=("sales", "sum"),
        profit=("profit", "sum")
    )
    .sort_values("sales", ascending=False)
    .head(10)
)

print(top_products)


# ==========================================
# 8. CREATE CHARTS FOLDER
# ==========================================

os.makedirs("charts", exist_ok=True)


# ==========================================
# 9. MONTHLY SALES CHART
# ==========================================

monthly_sales = (
    df.groupby("month")["sales"]
    .sum()
)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(range(1, 13))

plt.tight_layout()

plt.savefig(
    "charts/monthly_sales.png",
    dpi=300
)

plt.show()
plt.close()


# ==========================================
# 10. SALES BY REGION CHART
# ==========================================

region_sales = (
    df.groupby("region")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "charts/sales_by_region.png",
    dpi=300
)

plt.show()
plt.close()


# ==========================================
# 11. SALES BY CATEGORY CHART
# ==========================================

category_sales = (
    df.groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "charts/sales_by_category.png",
    dpi=300
)

plt.show()
plt.close()


# ==========================================
# 12. COMPLETION MESSAGE
# ==========================================

print("\n================================")
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("================================")