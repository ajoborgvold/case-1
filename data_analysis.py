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
# Sale per product; identify top 5 products
products = df.groupby("Category")["Product"].apply(lambda x: x.unique())
product_sales = df.groupby(["Category", "Product"]).apply(lambda x: (x["Units Sold"] * x["Sale Price"]).sum(), include_groups=False)
sorted_product_sales = product_sales.sort_values(ascending=False)
top_5_products_sale = sorted_product_sales.head(5)
bottom_5_products_sale = sorted_product_sales.tail(5)
# print(sorted_product_sales)
# print(top_5_products_sale)
# print(bottom_5_products_sale)

product_units_sold = df.groupby(["Category", "Product"])["Units Sold"].sum()
sorted_product_units_sold = product_units_sold.sort_values(ascending=False)
top_5_products_units = sorted_product_units_sold.head(5)
bottom_5_products_units = sorted_product_units_sold.tail(5)
# print(top_5_products_units)
# print(bottom_5_products_units)

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
total_sale_per_category = sale_per_row.groupby(df["Category"]).sum()
# print(total_sale_per_category)
#=================================#


#=================================#
# Seasonal trends in sale
datetime = pd.to_datetime(df["Sale Date"])

# Sale trends per month; total sale and units
total_sale_per_month = sale_per_row.groupby(datetime.dt.month_name()).sum()
units_sold_per_month = df["Units Sold"].groupby(datetime.dt.month_name()).sum()
# print(total_sale_per_month)
# print(units_sold_per_month)

# Sale trends per day; total sale and units
total_sale_per_day = sale_per_row.groupby(datetime.dt.date).sum()
units_sold_per_day = df["Units Sold"].groupby(datetime.dt.date).sum()
# print(total_sale_per_day)
# print(units_sold_per_day)

# Sale trends per month per category; total sale and units
total_sale_per_category_per_month = sale_per_row.groupby([df["Category"], datetime.dt.month]).sum()
units_sold_per_category_per_month = df.groupby([df["Category"], datetime.dt.month])["Units Sold"].sum()
# print(total_sale_per_category_per_month)
# print(units_sold_per_category_per_month)

# Sale trends per day per category; total sale and units
total_sale_per_category_per_day = sale_per_row.groupby([df["Category"], datetime.dt.date]).sum()
units_sold_per_category_per_day = df.groupby([df["Category"], datetime.dt.date])["Units Sold"].sum()
# print(total_sale_per_category_per_day)
# print(units_sold_per_category_per_day)

# Days with the highest/lowest sale, day average and median sale
sorted_total_sale_per_day = total_sale_per_day.sort_values(ascending=False)
top_day = sorted_total_sale_per_day.head(1)
bottom_day = sorted_total_sale_per_day.tail(1)
day_average = total_sale / len(total_sale_per_day)
median_sale = total_sale_per_day.median()
# print(top_day)
# print(bottom_day)
# print(f"Average sale per day: {day_average}")
# print(f"Median sale: {median_sale}")

#=================================#