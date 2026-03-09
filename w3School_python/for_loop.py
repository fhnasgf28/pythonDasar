# the continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'cherry':
        break
    print(x)

# the range() Fuction

for x in range(6):
    print(x)

print('==============')
# using the start parameter
for x in range(2, 6):
    print(x)

print('============')

for x in range(2, 30,3):
    print(x)

print('=============')
    #else in for loop
for x in range(7):
    print(x)
else:
    print('Finally Finished')

print('==========')
    #break
for x in range(5):
    if x == 3: break
    print(x)
else:
    print('Finally Finished')

    #Nested Loop
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)