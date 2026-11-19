import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

# 8. Order Status Analysis
query = """
SELECT
    order_status,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;
"""

result = pd.read_sql_query(query, conn)

print("\nOrder Status Analysis:")
print(result)

conn.close()A