import sqlite3

def calculate_sales():
    # Connect to the database (replace with actual database parameters)
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()

    # Execute a query to fetch sales data (replace 'sales_table' and 'amount' with your actual table name and column)
    cursor.execute('SELECT amount FROM sales_table')

    # Calculate total sales
    total_sales = sum(row[0] for row in cursor.fetchall())

    # Close the connection
    connection.close()

    return total_sales

# Example usage
total = calculate_sales()
print(f"Total Sales: {total}")