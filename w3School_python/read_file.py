f = open('demofile.txt', 'r')
print(f.read(6))

print(f.readline())

fa = open('demofile.txt', 'a')
fa.write('Now the file has more content')
fa.close()

# open and read the file after the appending:
fa = open('demofile.txt', 'r')
print(fa.read())