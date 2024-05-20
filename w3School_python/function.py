def my_function(fname):
    print(fname +' Hello from a function')

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

my_function2('Farhan','assegaf')

# Arbitrary Arguments, *args
def my_function3(*kids):
    print('the youngest child is' + kids[2])

my_function3('emil', 'Tobias', 'Linus')

# keyword argument
