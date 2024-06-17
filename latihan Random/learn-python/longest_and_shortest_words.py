word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"], ["assegaf", "bagus", "rahmat", "farhan","mega", "ikah"]

longest_word = word_list[0]
shortest_word = word_list[1]

for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word

print('Longest word\t:', longest_word)
print('Shortest word\t:', shortest_word)


longest_word = word_list[0]
shortest_word = word_list[0]

for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word

print("Longest word:", longest_word)
print("Shortest word:", shortest_word)