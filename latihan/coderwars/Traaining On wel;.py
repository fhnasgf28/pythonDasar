# def well(x):
#     # hitung berapa kali kata 'good' muncul dalam array x
#     count_good = x.count('good')
#
#     # berikan output sesuai dengan jumlah 'good yang ditemukan
#     if count_good == 1 or count_good == 2:
#         return 'Publish'
#     elif count_good > 2:
#         return 'I Smell A Serries'
#     else:
#         return 'Fail'
#
# print(well(['good', 'bad', 'good','good']))
# print(well(['bad', 'bad', 'good']))

def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'

print(well(['good', 'bad', 'good', 'bad']))
print(well(['bad', 'bad', 'bad']))
print(well(['good', 'good', 'good']))

print("============================================")

def well1(x):
    if 'good' in x:
        return 'I smell a series!' if x.count('good') > 2 else 'Publish!'
    else:
        return 'Fail!'

print(well1(['good', 'bad', 'good', 'bad']))
print(well1(['bad', 'bad', 'bad']))
print(well1(['good', 'good', 'good']))