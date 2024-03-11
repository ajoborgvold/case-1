import pandas as pd

df = pd.read_csv("tøjfirma_sales_data.csv")

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

for index, row in df[2:5].iterrows():
    print(f"Index: {index}. Product: {row['Product']}. Category: {row['Category']}.")

#==================#