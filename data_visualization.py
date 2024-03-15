import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

from data_analysis import total_sale_per_day, units_sold_per_day, total_sale_per_category, product_sales

def show_sales_per_day():
    dates = total_sale_per_day.index
    sales = total_sale_per_day.values
    units = units_sold_per_day.values

    fig, ax = plt.subplots(2, 1)

    ax[0].plot(dates, sales, linewidth=2.0)
    ax[0].set_xlabel("Date")
    ax[0].set_ylabel("Total sale")
    ax[0].set_title("Total sales per day")
    ax[0].tick_params(axis='x', rotation=45)
    ax[0].xaxis.set_major_formatter(DateFormatter("%d-%m"))

    ax[1].plot(dates, units, linewidth=2.0)
    ax[1].set_xlabel("Date")
    ax[1].set_ylabel("Units sold")
    ax[1].set_title("Total units sold per day")
    ax[1].tick_params(axis='x', rotation=45)
    ax[1].xaxis.set_major_formatter(DateFormatter("%d-%m"))
    
    
    plt.tight_layout()
    plt.show()

# show_sales_per_day()


def show_sale_per_category():
    fig, ax = plt.subplots()
    
    categories = total_sale_per_category.index
    values = total_sale_per_category.values
    colors = ['#eedd82', '#ff6666', '#90ee90']
    ax.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.set_title("Total sales distribution by category")
    
    plt.tight_layout()
    plt.show()

# show_sale_per_category()


def show_products_categories():
    fig, ax = plt.subplots()

    product_sales_pivot = product_sales.unstack()
    product_sales_pivot.T.plot(kind='bar', ax=ax, width=0.8)
    ax.set_xlabel('Product')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total Sales for each product with category differentiation')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

# show_products_categories()