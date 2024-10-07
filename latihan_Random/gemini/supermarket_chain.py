import csv
import pandas as pd

csv_path = r'A:\pythonDasar\latihan_Random\CSV\product.csv'
df = pd.read_csv(csv_path)
product_sales = {}
for index, row in df.iterrows():
    product_name = row['product_name']
    sale_amount = row['sale_amount']
    if product_name in product_sales:
        product_sales[product_name] += sale_amount
    else:
        product_sales[product_name] = sale_amount

# find the top 3 products with the highest total sales amaoun
top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:3]

# calculate the average sales amount per store for each of the top 3 product
for product, total_sales in top_products:
    product_df = df[df['product_name'] == product]
    store_sales = {}
    for index, row in product_df.iterrows():
        store_name = row['store_name']
        sale_amount = row['sale_amount']
        if store_name in store_sales:
            store_sales[store_name] += sale_amount
        else:
            store_sales[store_name] = sale_amount
    avg_sales_per_store = {store: sales / len(product_df) for store, sales in store_sales.items()}
    print(f"Product: {product}")
    print(f"Total Sales: {total_sales}")
    print(f"Average Sales per Store: {avg_sales_per_store}")
    print()