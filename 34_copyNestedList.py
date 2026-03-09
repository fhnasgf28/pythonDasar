data_0 = [1, 2, 4, 5, 6, 7, ]
data_1 = [3, 4, 5, 5, 7]

data_2d = [data_0, data_1]
data_2d_copy = data_2d.copy()

print(f'data 2d = {data_2d}')
print(f'data 2d copy = {data_2d_copy}')

# mengambil data dari nested list
data = data_2d[1][2]
print(f'data = {data}')

# address semuanya
print(f'address data 2d = {hex(id(data_2d))}')
print(f'address data 2d copy = {hex(id(data_2d_copy))}')

print('Address dari sumber ke-1')
print(f'address asli = {hex(id(data_2d[0]))}')
print(f'address copy = {hex(id(data_2d_copy[0]))}')

data_2d[1][0] = 5
data_2d[1] = 5
print(f'data = {data_2d}')
print(f'data copy = {data_2d_copy}')

# kita gunakan deepcopy
from copy import deepcopy

data_2d = [data_0, data_1,10]
data_2d_deepcopy = deepcopy(data_2d)

print(f'address asli = {hex(id(data_2d))}')
print(f'address deepcopy = {hex(id(data_2d_deepcopy))}')

print('address dari member ke-1')
print(f'address asli = {hex(id(data_2d[0]))}')
