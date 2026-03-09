# python inheritance
''' inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''


# Create a parent class

class Person5:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


#Use the person class to create an object, and then execute the printname method:
x = Person5("John", "Doe")
x.printname()


# create a child class
class Student(Person5):
    def __init__(self, fname, lname):
        # add the __init__() Function
        # Person5.__init__(self, fname, lname)
        #use the super() Function
        super().__init__(fname, lname)


x = Student("Farhan", "Assegaf")
x.printname()

# add properties
''' In the example below, the year 2019 should be a variable, 
and passed into the Student class when creating student objects. 
To do so, add another parameter in the __init__() function:'''


class Student1(Person5):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student1("Farhan1", "Farhan2", 2019)
print(x.graduationyear)


# add method
class Student(Person5):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()

# class Hero

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass
class Hero_strength(Hero):
    pass

lina = Hero('lina', 100)
techies = Hero_intelligent('techies',50)
axe = Hero_strength('axe',200)

print(lina.name)
print(techies.name)
print(axe.name)
