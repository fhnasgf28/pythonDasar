# Use the split() method to split a string into a list of words.
# Reverse each word from a list
# finally, use the join() function to convert a list into a string

def reverse_words(Sentence):
    # split string on whitespace
    words = Sentence.split(" ")

    # iterate list and reverse each word using ::-1
    new_word_llist = [word[::-1] for word in words]

    # joining the list of words
    res_str = " ".join(new_word_llist)
    return res_str

# given string
str1 = 'My Name is Farhan'
print(reverse_words(str1))
