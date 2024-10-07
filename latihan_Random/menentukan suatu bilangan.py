# # menginput angka
# angka = float(input("Tulis sebuah angka"))
# # menampilkan angka positif
# if angka > 0:
#     print("Angka Positif")
#
# elif angka == 0:
#     print("Angka Nol")
#
# # menampilkan kondisi angka negatif
# else:
#     print("angka Negatif")

'''' type hint untuk fungsi'''

# bentuk standar fungsi yang sudah kita pelajari

'''
study kasus 
'''

# penggunaan type hints
import string

def sepuluh_pangkat(argument:int) -> int:
    ''' FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    print(argument)
print("Ucup")