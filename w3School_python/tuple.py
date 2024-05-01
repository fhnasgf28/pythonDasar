# Python Tuples

# tuple allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# tuple length
print(len(thistuple))

# Create Tuple With One Item

# bukan tuple
thistuple1 = ("apple",)
print(type(thistuple1))

# not a tuple
thistuple2 = ("apple1")
print(type(thistuple2))

# tuple items - data types

# The tuple() Constructor

thistuple5 = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(thistuple5)

# Python - Access Tuple Items
print(thistuple5[2])

# Range of Indexes
print(thistuple5[2:5])
# check if item exists

if "apple" in thistuple5:
    print("Yes 'apple' is in the fruits tuple")