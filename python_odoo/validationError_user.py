# Define a function to calculate the monthly installment
def calculate_installment(principal, interest_rate, tenure):
    # Calculate the monthly interest rate
    monthly_interest_rate = interest_rate / 1200

    # Calculate the number of months
    num_months = tenure * 12

    # Calculate the monthly installment
    monthly_installment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** num_months / ((1 + monthly_interest_rate) ** num_months - 1)

    return monthly_installment

# Get user input for principal, interest rate, and tenure
principal = float(input("Enter the principal amount (in IDR): "))
interest_rate = float(input("Enter the interest rate (in %): "))
tenure = int(input("Enter the tenure (in years): "))

# Calculate and print the monthly installment
monthly_installment = calculate_installment(principal, interest_rate, tenure)
print("The monthly installment is approximately IDR {:.2f}".format(monthly_installment))