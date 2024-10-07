import random
from replit import clear
# from art import logo

def deal_card():
    cards = [11, 2, 4, 5, 6, 7, 8, 9, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and calculate the total"""

    # check for blackjack [Ace, 10] == [11, 10] == 21
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # check for 11 and replace it with 1 if the total is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, your opponent has a Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Dealing first 2 cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour Card: {user_cards}, and your total is: {user_score}.")
        print(f"\tComputer's first card is {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to deal another card, type 'n' to pass:")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {user_cards}, and final score: {user_score}.")
    print(f"\tComputer's final hand:{computer_cards}, and final score: {computer_score}.")
    print(compare_scores(user_score, computer_score))

    while input("Do you want to play a game of Blackjack? 'y' or 'n': ") == "y":
        clear()
        # print(logo)
        play_game()

    # Masih belum bekerja dengan baik