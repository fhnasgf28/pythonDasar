def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# contoh penggunaan
arr = [33, 10, 78, 91, 43, 21]
sorted_array = quick_sort(arr)
print("Sorted array:", sorted_array)