# Write a function to return True if
# the first and last number of a given list is same.
# If numbers are different then return False.

def first_last_same(numberList):
    print('Given List:', numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 50, 10]
print('result is', first_last_same(numbers_x))

numbers_y = [45, 67, 243, 89, 45]
print('result is')

