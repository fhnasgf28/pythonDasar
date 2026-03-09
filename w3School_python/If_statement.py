a = 200
b = 33

if b > a:
    print("b is grater than a")
else:
    print("b is not greather than a")

# short hand if

if a > b: print("a is greather than b")

# short hand if ... else
a = 2
b = 330

print("A") if a > b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

# Not
a = 33
b = 200

if not a > b:
    print("A is Not greater than B ")

    # python while loops
i = 1
while i < 6:
    print(i)
    i += 1

    # the break statement
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break

    # the else statement
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less then 6")

    # python For Loops