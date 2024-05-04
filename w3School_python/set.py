thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Get the length of set
print(len(thisset))

# set items - Data types
set1 = {"apple", "banana", "cherry", "mango"}
set2 = {1, 5, 7, 8, 10}
set3 = {True, False, False}

print(set1, set2, set3)

# type()

print(type(thisset))

#the set() contruktor

thisset1 = set(("apple", "banana", "cherry"))
print(thisset1)

# Python - Access Set Items
# Access Items

thisset1 = {"apple", "banana", "cherry"}

for x in thisset1:
    print(x)

# ================
print("banana" in thisset1)

print("cherry" not in thisset1)

# add items

thisset1.add("Orange2")
print(thisset1)

# add sets

tropical = {"pineapple", "mango", "papaya"}
thisset1.update(tropical)

print(thisset1)

# Add Any Iterable
myList = ["kiwi", "orange"]

thisset1.update(myList)
print(thisset1)