# Write a program to display only those numbers from a list that satisfy the following conditions
#
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 67, 34, 51, 89, 90, 54,600]

for item in numbers:
    if item > 500:
        break
    elif item > 1150:
        continue

    elif item % 5 == 0:
        print(item)