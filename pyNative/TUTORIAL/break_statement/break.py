numbers = [10, 40, 120, 230]
for i in numbers:
    if i > 100:
        break
    print('Current Number', i)

name = 'Jessaa19 joy'
size = len(name)
i = 0

while i < size:
    if name[i].isspace():
        break

    print(name[i], end= ' ')
    i = i + 1


# break nested loop
