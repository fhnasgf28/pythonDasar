num = int(input("Masukkan bilangan: "))

factorial = 1

if num < 0:
   print("Faktorial tidak terdefinisi untuk bilangan negatif")
elif num == 0:
   print("Faktorial dari 0 adalah 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("Faktorial dari",num,"adalah",factorial)
