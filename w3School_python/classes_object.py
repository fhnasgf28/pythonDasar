# create a class

class MyClass:
    x = 5

    #create object


p1 = MyClass()
print(p1.x)


# the __init__() function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = Person("John", 36)

print(p2.name)
print(p2.age)


# the __str__() function
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person1("John", 36)
print(p1)

# The __str__() Function
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
p2 = Person2("FARHAN", 23)
print(p2)

# object methods
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}")

p1 = Person3("farhanassegaf", 23)
p1.myfunc()

# the self parameter
# ternyata ga harus self, kita bisa menamainya apa yang kita inginkan

class Person4:
    def __init__(mysillyobject, name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Heloo my name is" + abc.name)
p1 = Person4("Farhan_4", 23)
p1.myfunc()
del(p1.age)

# Modify Object Properties