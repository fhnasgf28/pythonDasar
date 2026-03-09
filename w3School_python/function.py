def my_function(fname):
    print(fname + ' Hello from a function')

    #calling a function


my_function('Emil')
my_function('Tobias')
my_function('Linus')

#parameters or argumentt?
''' From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.'''


# number of arguments
def my_function2(fname, lname):
    print(fname + ' ' + lname)


my_function2('Farhan', 'assegaf')


# Arbitrary Arguments, *args
def my_function3(*kids):
    print('the youngest child is' + kids[2])


my_function3('emil', 'Tobias', 'Linus')


# keyword argument

def my_function(child, child2, child1):
    print('The Youngest child is' + child2)


my_function(child='faran', child1='assegaf', child2='farhan')


def my_function(**kid):
    print('His Last Name is' + kid['lname'])


my_function(fname='Tobias', lname='Refsnes')


# Default Parameter Value

def my_function(country='Norway'):
    print('I am from' + country)


my_function('sweden')
my_function('india')
my_function()
my_function('Brazil')


# Passing a List as an Argument

def my_function(food):
    for x in food:
        print(x)


fruits = ['apple', 'banana', 'cherry']

my_function(fruits)


# Return Value
def my_function(x):
    return 5 * x


print(my_function(5))
print(my_function(51))
print(my_function(15))
print(my_function(15))


# the pass statement
def farahan():
    pass


# positional-only-arguments
def my_function5(x):
    print(x)


my_function5(x=3)

# def my_function4(x, /):
#     print(x)
#
# my_function4(x = 3)

# keyword only argument
def my_function4(*, x):
    print(x)
my_function4(x = 5)

# Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print('==========Recursion=============')
tri_recursion(9)
