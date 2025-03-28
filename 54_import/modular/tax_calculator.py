def calculator_tax(income):
    if income <= 50000000:
        tax = income * 0.05
    elif income <= 250000000:
        tax = income * 0.15
    elif income <= 500000000:
        tax = income * 0.25
    else:
        tax = income * 0.30
    return tax

if __name__ == "__main__":
    income = int(input("Enter your income: "))
    print(f"Tax: , {calculator_tax(income):.2f}")
