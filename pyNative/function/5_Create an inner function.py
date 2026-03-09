# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it


def outer_func(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from autho function
    add = addition(a, b)

    return add + 5

result = outer_func(5, 10)
print(result)