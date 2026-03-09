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

# loop Through a tuple
for x in thistuple5:
    print(x)

# loop through the index numbers
for i in range(len(thistuple5)):
    print(thistuple5[i])

# using a while loop

# Change Tuple Values
change_value_tuple = list(thistuple5)
change_value_tuple[2] = "Jeruk"
thistuple5 = tuple(change_value_tuple)

print(thistuple5)

# Add Items
convert_tuple = list(thistuple5)

convert_tuple.append("Belimbing")
thistuple5 = tuple(convert_tuple)

print(thistuple5)

# add tuple to a tuple
add_tuple = ("Jeruk Nipis",)
thistuple5 += add_tuple

print(thistuple5)

# Remove Items Tuple

remove_tuple = list(thistuple5)
remove_tuple.remove("Belimbing")
thistuple5 = tuple(remove_tuple)

print(thistuple5)

# python - unpack tuples

# Unpacking a Tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(tropic, *red) = fruits

print(tropic)
print(red)

# Python - Loop Tuples
for i in range(len(fruits)):
    print(fruits[i])

    # using a while Loop
i = 0
while i < len(fruits):
    print(fruits[1])
    i = i + 1