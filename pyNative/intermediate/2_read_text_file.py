# First, read a text file.
# Next, use string replace() function to replace all newlines (\n) with space (' ').

# Steps to solve this question: -
#
# First, open the file in a read mode
# Next, read all content from a file using the read() function and assign it to a variable.
# Next, use string replace() function to replace all newlines (\n) with space (' ').
# Display final string

with open('sample.txt', 'r') as file:
    data = file.read().replace('\n',' ')
    print(data)

