# copy dictionary

teman_teman = {
    'ucup': 'otong surotong',
    'otong': 'ucup surucup',
    'joko': 'wati susilawati',
    'wati': 'joko surojoko'
}

friends = teman_teman.copy()
print(friends)

print('teman-teman\t:', teman_teman)
print(f'teman-teman\t: {teman_teman}')
print(f'friends\t: {friends} \n')

teman_teman['cup'] = 'ucup si kweren'
print(f'teman-teman\t: {teman_teman}\n')
print(f'friends\t: {friends} \n')

# pop dictionary (yang terakhir ajah)

data_terakhir = friends.popitem()
print(f'data terakhir\t: {data_terakhir}')
print(f'friends\t: {friends} \n')