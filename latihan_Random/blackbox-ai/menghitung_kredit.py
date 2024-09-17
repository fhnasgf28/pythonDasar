def calculate_installment(principal, interest_rate, tenure):
    monthly_interest_rate = interest_rate / 1200

    # calculate the number of month
    num_months = tenure * 12

    # calculate the monthly intallment
    monthly_installmen = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** num_months / ((1 + monthly_interest_rate) ** num_months - 1)

    return monthly_installmen

principal = float(input("Enter the principal amount (in IDR): "))
interest_rate = float(input("Enter the interest rate (in %): "))
tenure = int(input("Enter the tenure (in Years): "))

# calculate and print the monthly installment
monthly_installment = calculate_installment(principal, interest_rate, tenure)
print("The monthly installment is approximately IDR {:.2f}".format(monthly_installment))