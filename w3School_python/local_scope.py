def myfunc():
    x = 300
    print(x)


myfunc()


# function inside function
def myfunct1():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunct1()

# global scope
x = 303


def myfunct2():
    print(x)


myfunct2()
print(x)

# naming variable
xx = 400


def myfunc3():
    x = 200
    print(x)


myfunc3()
print(xx)


# global keyword
def myfunc4():
    global x
    x = 30056


myfunc4()
print(x)

# non local keyword
def myfunct6():
    x = 'Jane'
    def myfunct7():
        nonlocal x
        x = 'hello'
    myfunct7()
    return x

print(myfunct6())