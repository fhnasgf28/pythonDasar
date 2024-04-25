b = 200
c = 33

if b > c:
    print("B is greater than C")
else:
    print("b is not greater than a")


# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

# Most Values are True
bool("Makanan")
bool(123)
bool(["Apple", "Cherry", ["banana"]])

# Functions can Return a Boolean
def myFunction():
    return True

if myFunction():
    print("YES")
else:
    print("NO")

print(myFunction())

x = 200
print(isinstance(x, int))