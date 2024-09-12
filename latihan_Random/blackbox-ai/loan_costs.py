def calculate_loan_cost():
    loan_amount = float(input("Enter the loana amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    number_of_years = int(input("Enter the number of years: "))

    # calculate the total cost of the loan
    total_cost = loan_amount * (1 + annual_interest_rate/100) ** number_of_years

    print("The otal cost of the loan after {} years is: {}".format(number_of_years, total_cost))

calculate_loan_cost()
