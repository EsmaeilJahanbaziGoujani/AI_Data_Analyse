# import pandas as pd  # Imports the pandas library for data manipulation and analysis
# import matplotlib.pyplot as plt  # Imports matplotlib for plotting graphs
#
# x = pd.read_csv('sales.csv')  # Reads the 'sales.csv' file into a DataFrame called x
#

# x['Revenue'] = x['Price'] * x['Quantity']  # Creates a new column 'Revenue' by multiplying 'Price' and 'Quantity' for each row
#
# grouped = x.groupby(['Date', 'Product'])['Revenue'].sum().reset_index()  # Groups by 'Date' and 'Product', then sums 'Revenue' for each group and resets index to create a summarized DataFrame, sums the 'Revenue' for each group, and resets the index
# # sum().reset_index():  # Sums values for each group and turns group keys ('Date', 'Product') from index back into columns
#
# print(grouped)  # Prints the grouped DataFrame to show total revenue per product per date
#
# products = grouped['Product'].unique()  # Extracts all unique product names from the grouped DataFrame for iteration
#
# for product in products:  # Iterates over each unique product
#     product_data = grouped[grouped['Product'] == product]  # Filters the grouped DataFrame to only include rows for the current product
#     plt.plot(product_data['Date'], product_data['Revenue'], marker='*', label=product)  # Plots 'Date' vs. 'Revenue' for this product as a line with star markers and adds a label for the legend
#
# plt.xlabel('Date')  # Sets the label for the x-axis to 'Date'
# plt.ylabel('Revenue')  # Sets the label for the y-axis to 'Revenue'
# plt.title('Daily Revenue per Product')  # Sets the title of the plot
# plt.legend()  # Displays a legend to identify each product's line
# plt.xticks(rotation=45)  # Rotates the x-axis labels by 45 degrees for better readability
# plt.tight_layout()  # Adjusts the layout to prevent overlap
# plt.show()  # Displays the plot
