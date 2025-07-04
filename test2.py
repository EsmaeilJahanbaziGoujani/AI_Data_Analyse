import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file
df = pd.read_csv("sales.csv")

# 2. Calculate revenue for each row
df["Revenue"] = df["Price"] * df["Quantity"]

# 3. Group data by date and product, and sum the revenues
daily_sales = df.groupby(["Date", "Product"])["Revenue"].sum().unstack()

# 4. Plot the chart
daily_sales.plot(kind="bar", figsize=(10, 6), title="Daily Revenue by Product")
plt.xlabel("Date")
plt.ylabel("Revenue (currency unit)")
plt.grid(True)
plt.tight_layout()
plt.show()