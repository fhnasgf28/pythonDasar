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

# Python - Join Sets
set4 = set1.union(set2)
print(set4)

set4_a = set1 | set2
print(set4_a)

# Join Multiple Sets
set3_b = {"John", "Elena"}
set4_b = {"Apple", "Bananas", "Cherry"}

mySet = set1.union(set2, set3_b, set4_b)
print(mySet)

# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)

# =============== UPDATE ==========
set1.update(set2)
print(set1)

# Intersection
set5 = {"apple", "banana", "cherry"}
set6 = {"google", "microsoft", "apple"}

set7 = set5 & set6
print(set7)

# Difference
set7 = set5.difference(set6)
print(set7)

set7 = set5 - set6
print(set7)

# difference_update()
set5.difference_update(set6)
print(set5)