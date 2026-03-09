""" panjang = int(input('Masukan panjang deret:'))

fibo = [0,1]

for i in range(2, panjang):
    index = i - 2 
    index1 = i - 1 
    angkaSelanjutnya = index + index1

    fibo.append(angkaSelanjutnya)
    print(fibo)
     """

def fibonacci(n):
    if n < 1:
        return [n]
    
    listSebelumN = fibonacci(n - 1)
    angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
    angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

    print('listSebelumN', listSebelumN)
    print(f'angka1: {angka1}, angka2: {angka2}')

    return listSebelumN + [angka1 + angka2]