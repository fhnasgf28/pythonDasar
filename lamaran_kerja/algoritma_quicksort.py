def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


# contoh penggunaan
array1 = [3, 4, 6, 2, 6, 9, 2]
sorted_array = quicksort(array1)
print('array yang diurutkan:', sorted_array)
