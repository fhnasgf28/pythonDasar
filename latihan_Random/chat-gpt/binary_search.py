def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 # target tidak ditemukan

# contoh penggunaan
sorted_arr = [4, 56, 23, 56, 2, 5]
target = 23
target_index = binary_search(sorted_arr, target)
print("Index of target:", target_index)