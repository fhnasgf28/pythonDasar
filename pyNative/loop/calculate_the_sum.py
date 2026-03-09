# Approach 1: Use for loop and range() function
#
# Create variable s = 0 to store the sum of all numbers
# Use Python 3’s built-in function input() to take input from a user
# Convert user input to the integer type using the int() constructor and save it to variable n
# Run loop n times using for loop and range() function
# In each iteration of a loop, add current number (i) to variable s
# Use the print() function to display the variable s on screen
# Approach 2: Use the built-in function sum(). The sum() function calculates the addition of numbers in the list or range

s = 0
n = int(input("Enter Number"))

for i in range(1, n + 1, 1):
    s += i

print("\n")
print("Sum is: ", s)

# contoh 2
m  = int(input("Enter number"))
x = sum(range(1, m + 1))
print('sum is:', x)