thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# allow duplicates
# list length
print(len(thislist))

# List Items - Data Types
list0 = ["apple", "banana", "cherry"]
list1 = [3, 4, 5, 6, 7]
list2 = [True, False, True]

list4 = ["ABC", 34, True, 40, "male"]

# type

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
thislist1 = list(("apple", "banana", "cherry"))
print(thislist1)

# Python - Access List Items
thislist2 = ["apple", "banana", "cherry"]
print(thislist2[1])
print(thislist2[-2])

# range of indexes
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:4])
print(thislist[:4])
print(thislist2[2:])

# Check if Item Exists

if "apple" in thislist2:
    print("yes, 'apple' is in the fruits list")

# ++++++++++++ Python - Change List Items


# Change Item Value
thislist2[3] = "Blackcurrent"
print(thislist2)

# Change a Range of Item Values
thislist2[1:3] = ["blackcurrent", "Watermelon"]
print(thislist2)

# insert items
thislist2.insert(2, "watermellon")

# ================Python - Add List Items============
thislist2.append("orange")
print(thislist2)

# extend items
tropical = ["mango", "pineaplle", "papaya"]
thislist2.extend(tropical)
print(thislist2)

# Add Any Iterable

# Python - Remove List Items
thislist3 = ["apple", "banana", "cherry", "mango"]
thislist3.remove("banana")
print(thislist3)

# Remove Specified Index
thislist3.pop()
print(thislist3)

del thislist3

# Python - Loop Lists
thislist4 = ["apple", "banana", "Cherry", "Mango"]
for x in thislist4:
    print(x)

# Python - Sort Lists

# Sort List Alphanumerically
thislist4.sort(reverse=True)
print(thislist4)

# numerically:
thislist5 = [100, 200, 300, 400, 500]
thislist5.sort(reverse=True)
print(thislist5)


# Customize sort function
def myFunc(n):
    return abs(n - 200)


thislist5.sort(key=myFunc)
print(thislist5)

# Case Insensitive Sort
thislist6 = ["banana", "Orange", "Kiwi", "cherry"]
thislist6.sort(key=str.lower)
print(thislist6)

# reverse Order
thislist6.reverse()
print(thislist6)

# Python - Copy Lists
mylist1 = thislist6.copy()
print(mylist1)

mylist1 = list(thislist6)
print(mylist1)

# Python - Join Lists
# Join Two Lists
list5 = ["a", "b", "c", "d"]
list6 = [1, 2, 3]

list7 = list5 + list6
print(list7)

for x in list5:
    list6.append(x)

print(list6)

# method extend

list5.extend(list6)
print(list5)
