import random
from encodings.punycode import insertion_unsort
from os import remove


def deal_card():
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cartas)
    return card



def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return  sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Empate")
    elif computer_score == 0:
        print(f"Dealer has ab blackjack. You lose")
    elif user_score == 0:
        print(f"You win with Blackjack")
    elif user_score > 21:
        print(f"You lose")
    elif computer_score > 21:
        print(f"You win")
    elif user_score > computer_score:
        print(f"You win")
    else:
        print("You lose")

def play():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True

        if input("Do you want to draw another card? (Y/N") == "Y":
            user_cards.append(deal_card())
        else:
            game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Keep playing (Y/N)") == "Y":
    print("\n" * 20)
    play()