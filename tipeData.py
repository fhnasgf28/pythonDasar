data_integer = 1
print ("data :", data_integer)
print ("- bertipe :", type(data_integer))

# tipe data angka dengan koma (float)
data_float = 1.5
print ("data :", data_float)
print ("- bertipe :", type(data_float))

# tipe data string
data_string = "nama saya farhan"	
print ("data :", data_string)
print ("- bertipe :", type(data_string))

# tipe data boolean
data_boolean = True
print ("data :", data_boolean)
print ("- bertipe :", type(data_boolean))

# tipe data khusus

# bilangan kompleks
data_complex = complex (6,5)
print ("data :", data_complex)
print ("- bertipe :", type(data_complex))

# tipe data dari bahasa c
# kita harus mengimport terlebih dahulu
from ctypes import c_double, c_char

data_c_double = c_double (10.5)
print ("data :", data_c_double)
print ("- bertipe :", type(data_c_double))
