# call function with 3 argument
# To accept a variable length of positional arguments, i.e.,
# To create functions that take n number of positional arguments we use *args as a parameter. (prefix a parameter name with an asterisk * ).
#
# Using this, we can pass any number of arguments to
# this function. Internally all these values are represented in the form of a tuple.
#

def funct1(*args):
    for i in args:
        print(i)
funct1(80, 100)
funct1(30,50,60,70)

