for i in range(10):
    print(i, end= ' ' )

print('============================')
# range(start, stop)
for o in range(10, 16):
    print(o, end=' ')
print('\n============')
# range(start, stop, step)
for i in range(10, 50, 5):
    print(i, end=' ')


for h in range(9, 100, 3):
    print(h, end=' ')

# for loop with range()
for i in range(1, 10, 2):
    print("Current value of i is:", i)

# iterate a list using range() and for loop
list1 = ['Jessa', 'Emma', 20, 30, 75.5]

for i in range(len(list1)):
    print(list1[i])
