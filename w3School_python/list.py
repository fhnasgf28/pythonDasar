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
