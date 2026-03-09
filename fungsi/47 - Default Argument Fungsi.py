''' Default Argument'''


# def fungsi(argument)
# def fungsi(argument = nilai defaultnya)

# contoh 1
def say_hello(nama="ganteng"):
    ''' fungsi dengan default argument '''
    print(f'Hallo{nama}')


say_hello('farhan')
say_hello()


# contoh 2
def hitung_pangkat(angka, pangkat=2):
    hasil = angka ** pangkat
    return hasil


print(hitung_pangkat(3))
print(hitung_pangkat(3, 3))

hasil = hitung_pangkat(pangkat=3, angka=3)
print(hasil)


# contoh 4
def fungsi(input1=1, input2=2, input3=3, input4=4):
    '''fungsi dengan default argument'''
    hasil = input1 + input2 + input3 + input4
    return hasil


print(fungsi())
print(fungsi(input3=10))
print(fungsi(1, 2, 3, 4))
