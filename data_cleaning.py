import pandas as pd

df = pd.read_csv("tøjfirma_sales_data.csv")


#==============================#
# Check for missing values and empty rows. Remove any empty rows
missing_values = df.isna().sum()
# print(missing_values)
empty_rows_dropped = df.dropna(how='all')
# print(empty_rows_dropped)
#==============================#



#==============================#
# Check for duplicates and drop them if there are any
duplicates = df.duplicated()
# print(duplicates)
duplicates_dropped = df.drop_duplicates()
# print(duplicates_dropped)
#==============================#



#==============================#
# Check data validity for all columns in the data set
data_types = df.dtypes
# print(data_types)
# This shows that Units Sold contains only integers and Sale Price contains only floats.

min_units_sold = df["Units Sold"].min()
# print(min_units_sold)
# This proves that the lowest integer in Units Sold is 1, i.e. all values are positive and thereby valid.

min_sale_price = df["Sale Price"].min()
# print(min_sale_price)
# This proves that the lowest Sale Price is is 8.0, i.e. all values are positive and thereby valid.

unique_categories = df["Category"].unique()
# print(unique_categories)
# This shows that there are three unique categories: Children, Men and Women. The most reasonable assumption is that these three are all valid category values and thereby that all category values are valid.

unique_sizes = df["Size"].unique()
# print(unique_sizes)
# This shows that there are six unique sizes: XS, S, M, L, XL, XXL. The most reasonable assumption is that these are all valid sizes and thereby that all size values are valid.

unique_products = df["Product"].unique()
# print(unique_products)
# This shows that there are 10 unique products: Shorts, Jeans, Skirt, Jacket, Hat, Sweater, Dress, Hoodie, T-Shirt and Socks. The most reasonable assumption is that these are all valid product values and thereby that all product values are valid.

# try:
#     df["Sale Date"] = pd.to_datetime(df["Sale Date"])
#     print("All Sale Date values are valid dates and times")
# except ValueError as e:
#     print(f"Error: {e}")
#     print("Not all Sale Date values are valid dates and times")
# This proves that all Sale Date values are valid dates and times

#==============================#



#==============================#
# Conclusion:
# There is nothing to clean. The data set is ready for analysis.
#==============================#