import pandas as pd

df = pd.read_csv("../tøjfirma_sales_data.csv")

#==================#
# Get the first x rows; x in square brackets

first_10_rows = df.head(10)
# print(first_10_rows)

#==================#


#==================#
# Get a specific column from column heading

products = df["Product"]
# print(products)
#==================#


#==================#
# Get row by index
# – Headings are not included ==> Starting from index 1 means starting from the first data row
# – Up to but not including the value after colon

selected_rows = df[1:5]
# print(selected_rows)
#==================#


#==================#
# Iterate through columns

# for column in df.columns:
#     print(f"Column name: {column}")

#==================#


#==================#
# Iterate through columns

# for index, row in df[2:5].iterrows():
#     print(f"Index: {index}. Product: {row['Product']}. Category: {row['Category']}.")

#==================#


#==================#
# Desribe the data

describe_data = df.describe()
print(describe_data)

data_info = df.info()
print(data_info)

# Get info about non-numeric values
# describe_include = df.describe(include=["object", "category"])
# print(describe_include)

#==================#


#==================#
# Calculate sales

# Assuming that the sale price is for all units sold
mean_without_units = df["Sale Price"].mean()
# print("Mean, without units count", mean_without_units)

# Assuming that the sale price is per unit
product_sales_price = df["Sale Price"] * df["Units Sold"]
mean_with_units = product_sales_price.mean()
# print("Mean, with units count", mean_with_units)



#==================#