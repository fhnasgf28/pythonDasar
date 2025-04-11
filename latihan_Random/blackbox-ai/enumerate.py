# daftar buah
buah = ["apel", "jeruk", "mangga", "pisang"]
for index, buah in enumerate(buah):
    print(f"{index+1}. {buah}")


# daftar sayuran
sayuran = ["tomat", "buncis", "kangkung", "selada"]
for index, vegetable in enumerate(sayuran, start=1):
    print(f"{index}. {vegetable}")