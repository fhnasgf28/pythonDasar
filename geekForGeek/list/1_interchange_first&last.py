# Given a list, write a Python program to swap first and last element of the list.

# Given a list, write a Python program to swap first and last element of the list.

def swaplist(newlist):
    size = len(newlist)

    # swapping
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist

# driver code
newList = [12,35,9,56,24]
print(swaplist(newList))

# swap function

def swaplist1(newlist1):
    newlist1[0], newlist1[-1] = newlist1[-1], newlist1[0]

    return newlist1

# driver code
newList1 = [12,35, 56, 24]
print(swaplist1(newList1))