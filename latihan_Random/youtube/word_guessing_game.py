import random
import re

def read_words():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print("File 'words.txt' not found.")
        return []

def display_word(secret_word, guessed_letters):
    word_to_display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += "_"

    return word_to_display

def get_guess(guessed_letters):
    while True:
        guess = input("enter a letter: ").lower()
        if len(guess) != 1:
            print("Enter only one letter.")
        elif not re.search("^[a-z]$", guess):
            print("Enter only letters from a to z.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def main():
    words = read_words()
    if not words:
        print("No words found in 'words.txt'.")
        return

    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("Attempts left:", attempts)
        print("Word:", display_word(secret_word, guessed_letters))
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess.")

        if is_word_guessed(secret_word, guessed_letters):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print("You lost. The word was:", secret_word)

if __name__ == "__main__":
    main()