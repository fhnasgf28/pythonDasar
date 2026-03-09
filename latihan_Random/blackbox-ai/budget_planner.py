budget = {}

# ask the user to input their salary
salary = int(input("Enter your salary: "))

# ask the user to input their budget for each category
print("Enter your budget for each category: ")
categories = ['rent', 'food', 'transportation', 'entertainment', 'saving', 'others']
for category in categories:
    budget[category] = int(input(f"Enter budget for {category}: "))

# ask the user to input their actual expenses for each category
print("Enter your actual expenses for each category: ")
actual_expenses = {}
for category in categories:
    actual_expenses[category] = int(input(f"Enter actual expense for {category}: "))

# calculate the total expenses for each category
total_expenses = {}
for category in categories:
    total_expenses[category] = actual_expenses[category]

# check if the user exceeded their budget for each category
for category in categories:
    if total_expenses[category] > budget[category]:
        print(f"Alert: You exceeded your budget for {category} by {total_expenses[category] - budget[category]}")

# Display a summary of the user's expenses and budget
print("Summary:")
for category in categories:
    print(f"{category.capitalize()}: Budget={budget[category]:,}, Actual={total_expenses[category]:,}")