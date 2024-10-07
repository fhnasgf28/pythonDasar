# Set counter = 0
# Run while loop till number != 0
# In each iteration of loop
# Reduce the last digit from the number using floor division ( number = number // 10)
# Increment counter by 1
# print counter
num = 75869567
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:\t", count)