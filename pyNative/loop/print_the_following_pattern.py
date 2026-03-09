# Set row = 5 because the above pattern contains five rows
# create an outer loop to iterate numbers from 1 to 5 using for loop and range() function
# Create an inner loop inside the outer loop in such a way that in each iteration of the outer loop, the inner loop iteration will be reduced by i. i is the current number of an outer loop
# In each iteration of the inner loop, print the iterator variable of the inner loop (j)
# Note:
#
# In the first iteration of the outer loop inner loop execute five times.
# In the second iteration of the outer loop inner loop execute four times.
# In the last iteration of the outer loop, the inner loop will execute only once

n = 5
k = 5
for i in range(0, n + 1):
    for j in range(k-i, 0, -1):
        print(j, end=' ')
    print()


# Fungsi range():
# Fungsi range() digunakan untuk menghasilkan urutan bilangan bulat.
# Format umumnya adalah range(start, stop, step), di mana:
# start: Nilai awal urutan (termasuk).
# stop: Nilai akhir urutan (tidak termasuk).
# step: Nilai penambahan antara setiap elemen dalam urutan (opsional, default = 1).