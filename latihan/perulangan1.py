number = input("Enter a number\t:")

try:
    n = int(number)
except:
    print("Invalid Input")
    exit()

# check if number is negative

if n < 0 :
    print("Invalid Input")
    exit()

factorial = 1 

for i in range(1, n + 1):
    factorial = n * factorial

print(f"The Factorial of {n} is {factorial}")