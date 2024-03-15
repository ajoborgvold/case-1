from data_cleaning import *
from data_analysis import *

while True:
    print("Select which part of the data you want to inspect:")
    print("1) Data cleaning.")
    print("2) Data analysis.")
    print("3) Quit.")
    user_selection = input("Enter a number from the list above:\n")
    user_selection = user_selection.strip()
    
    if user_selection == "1":
        print()
        print("Select which part of the data cleaning process you want to inspect:")
        print("a) Preliminary data types check.")
        print("b) Missing values.")
        print("c) Detaled data types check.")
        print("d) Return to main menu.")
        print()
        cleaning_selection = input("Enter a letter from the list above:\n")
        cleaning_selection = cleaning_selection.strip().lower()
        print()
        
        if cleaning_selection == "a":
            print(data_types)
            print()
        elif cleaning_selection == "b":
            print(missing_values)
            print()
        elif cleaning_selection == "c":
            print(f"Minimum value for units sold: {min_units_sold}")
            print()
            print(f"Minimum value for sale price: {min_sale_price}")
            print()
            print(f"All unique categories:\n {unique_categories}")
            print()
            print(f"All unique sizes:\n {unique_sizes}")
            print()
            print(f"All unique products:\n {unique_products}")
            print()
            print("Conclusion: All values are valid and seem appropriate/reasonable.")
            print()
        elif cleaning_selection == "d":
            continue
        else:
            print(f"Invalid selection. You entered: {cleaning_selection}. Please try again.")
            print()
        
    elif user_selection == "2":
        print()
        print("Select which part of the data analysis you want to inspect:")
        print("a) Total, average and median sale.")
        print("b) Sale distributed on products.")
        print("c) Sale distributed on categories.")
        print("d) Sale over time.")
        print("e) Return to main menu.")
        print()
        analysis_selection = input("Enter a letter from the list above:\n")
        analysis_selection = analysis_selection.strip().lower()
        print()
        
        if analysis_selection == "a":
            print(f"Total sale: {total_sale}")
            print()
            print(f"Average sale per day: {day_average}")
            print()
            print(f"Median sale per day: {median_sale}")
            print()
        elif analysis_selection == "b":
            print(f"Sale per product in descending order:\n {sorted_product_sales}")
            print()
            print(f"Top five products, based on sale:\n {top_5_products_sale}")
            print()
            print(f"Bottom five products, based on sale:\n {bottom_5_products_sale}")
            print()
            print(f"Top five products, based on units sold:\n {top_5_products_units}")
            print()
            print(f"Bottom five products, based on units sold:\n {bottom_5_products_units}")
            print()
        elif analysis_selection == "c":
            print(f"Total sale per category:\n {total_sale_per_category}")
            print()
            print(f"Units sold per category:\n {units_sold_per_category}")
        elif analysis_selection == "d":
            print(f"Total sale per month: {total_sale_per_month}")
            print()
            print(f"Total sale per day: {total_sale_per_day}")
            print()
            print(f"Top day:\n {top_day}")
            print()
            print(f"Bottom day:\n {bottom_day}")
        elif analysis_selection == "e":
            continue
        else:
            print(f"Invalid selection. You entered: {analysis_selection}. Please try again.")
            print()
        
    elif user_selection == "3":
        break
    else:
        print()
        print(f"Invalid selection. You entered {user_selection}. Please try again.")
        print()