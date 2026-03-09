from decimal import Decimal, getcontext, ROUND_HALF_UP

# Set the precision for decimal calculations to avoid errors.
# This ensures a consistent number of decimal places for currency.
getcontext().prec = 28 # Set a high precision for calculations
TWO_PLACES = Decimal("0.01")

def calculate_weekly_pay(hourly_wage, hours_worked):
    """
    Calculates the total weekly pay using the Decimal module for accuracy.

    Args:
        hourly_wage (str): The employee's hourly wage as a string.
        hours_worked (str): The number of hours worked as a string.

    Returns:
        Decimal: The calculated total earnings.
    """
    try:
        # Convert string inputs to Decimal for exact arithmetic
        wage = Decimal(hourly_wage)
        hours = Decimal(hours_worked)
        earnings = wage * hours
        # Round the result to two decimal places
        return earnings.quantize(TWO_PLACES, rounding=ROUND_HALF_UP)
    except Exception as e:
        print(f"Error during calculation: {e}")
        return None

def format_currency(amount, currency_symbol="$"):
    """
    Formats a Decimal amount as a currency string with a thousands separator.

    Args:
        amount (Decimal): The amount of money to format.
        currency_symbol (str): The symbol for the currency (e.g., "$", "€").

    Returns:
        str: The formatted currency string.
    """
    if amount is None:
        return "N/A"
    return f"{currency_symbol}{amount:,.2f}"

# Get user input for calculation
employee_name = input("Enter the employee's name: ")
wage_input = input("Enter the hourly wage (e.g., '15.50'): ")
hours_input = input("Enter the hours worked this week (e.g., '40'): ")

# Perform the calculation and format the output
weekly_pay = calculate_weekly_pay(wage_input, hours_input)

if weekly_pay is not None:
    formatted_pay = format_currency(weekly_pay)
    print(f"\n{employee_name}'s total earnings this week are: {formatted_pay}")

