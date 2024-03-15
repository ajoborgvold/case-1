from data_analysis import total_sale, average_sale_per_row, day_average, top_day, top_5_products_sale, total_sale_per_category, bottom_day, median_sale

def create_report():
    print("Conclusion regarding data quality:\n - No missing values or empty rows.\n - No duplicates to remove.\n - No invalid or odd values.\n The data is ready for analysis.")
    print()
    print(f"Total and average sale:\n - Total sale: {total_sale}\n - Average sale per row: {average_sale_per_row}\n")
    print()
    print(f"Sale based on products and categories:\n - Top five products:\n {top_5_products_sale}\n - Total sale per category:\n {total_sale_per_category}")
    print()
    print(f"Sale trends over time:\n Top day:\n {top_day}\n - Bottom day:\n {bottom_day}\n - Average sale per day: {day_average}\n - Median sale per day: {median_sale}")
    
create_report()