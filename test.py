# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# x = pd.read_csv("sales.csv")
#
# x["Revenue"] = x["Price"] * x["Quantity"]
#
# grouped = x.groupby(["Date", "Product"])["Revenue"].sum().reset_index()
# print(grouped)
#
# products = grouped["Product"].unique()
#
# for product in products:
#     product_data = grouped[grouped["Product"] == product]
#     plt.plot(product_data["Date"], product_data["Revenue"], marker="*", label=product)
#
# plt.xlabel("Date")
# plt.ylabel("Revenue")
# plt.title("Daily Revenue per Product")
# plt.show()
#
