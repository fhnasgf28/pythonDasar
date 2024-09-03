def get_sales_data():
    product_name = input("Enter Product Name: ")
    try:
        #get the quantity sold and price per unit from the user
        #(TO DO: add error handling for invalid inputs)
        quantity_sold = int(input("Enter quantity sold: "))
        price_per_unit = float(input("Enter Price Per Unit: "))
        return product_name, quantity_sold, price_per_unit
    except ValueError:
        pass


def calculate_sales_revenue(quantity_sold, price_per_unit):
    return quantity_sold * price_per_unit


#main program
product_name, quantity_sold, price_per_unit = get_sales_data()
total_sales_revenue = calculate_sales_revenue(quantity_sold, price_per_unit, )
print(f"Total sales revenue: {total_sales_revenue:.2f}")
