import pandas as pd

df = pd.read_csv("tøjfirma_sales_data.csv")

#=================================#
# Calculate total sale and average sale:
sale_per_row = df["Units Sold"] * df["Sale Price"]
total_sale = sale_per_row.sum()
average_sale_per_row = sale_per_row.mean()
# print(total_sale)
# print(average_sale_per_row)
#=================================#


#=================================#
# Identify top 5 products:
top_5_by_sale = df.loc[sale_per_row.nlargest(5).index]
top_5_by_quantity = df.loc[df["Units Sold"].nlargest(5).index]
# print(top_5_by_sale)
# print(top_5_by_quantity)
#=================================#


#=================================#
# Identify patterns related to gender
# Count products in the three categories
count_products_children = (df["Category"] == "Children").sum()
count_products_women = (df["Category"] == "Women").sum()
count_products_men = (df["Category"] == "Men").sum()
# print(count_products_children)
# print(count_products_women)
# print(count_products_men)

# Count units sold in the three categories
units_sold_per_category = df.groupby("Category")["Units Sold"].sum()
# print(units_sold_per_category)
#=================================#


#=================================#
# Seasonal trends in sale
datetime = pd.to_datetime(df["Sale Date"])
print(datetime)

#=================================#