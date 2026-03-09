# To access a range of items in a list, use the slicing operator :. With this operator, you can specify where to start the slicing, end, and specify the step.
#
# For example, the expression list1[ start : stop : step] returns the portion of the list from index start to index stop, at a step size step.
#
# for 1st list: Start from the 1st index with step value 2 so it will pick elements present at index 1, 3, 5, and so on
# for 2nd list: Start from the 0th index with step value 2 so it will pick elements present at index 0, 2, 4, and so on

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_element = l1[1::3]
print("Element at odd-index positions from list one")
print(odd_element)

even_elements = l2[2::4]
print("Element at even-index positions from list two")
print(even_elements)

