i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'am in if Block")
else:
    print("i is greater then 15")
    print("i'am in else block")


def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum


# initialZING LIST
List = [367, 111, 562, 945, 6726, 873]

# using the function on odd elemets of the list
newList = [digitSum(i) for i in List if i & 1]
print(newList)
