import os
import random
import art


def deck_total(deck):
    # TODO 4: Calculate the user's and computer's scores based on their card values
    total = 0
    for card in deck:
        total += card
    return total


def check_blackjack(deck):
    """ Function will take deck as input and return true if it's blackjack else false"""
    # TODO 2: Detect when computer or user has a blackjack. (Ace + 10 value card).
    total = deck_total(deck)
    if total == 21:
        return True
    else:
        return False


def card_draw(original_deck, insertion_deck):
    """Function will take original deck and user/computer deck and return the updated user/computer deck"""
    insertion_deck.append(random.choice(original_deck))
    return insertion_deck


def replace_ace_value(deck):
    """Function will take user_deck and will replace ace value of 11 with 1 if deck total exceeds 21 adn return deck"""
    if deck_total(deck) > 21 and 11 in deck:
        index_of_ace = deck.index(11)
        deck[index_of_ace] = 1
    return deck


def win_lose(winner):
    """Function will take a bool value represent whether user win the game or lose the game"""
    # TODO 3: If computer gets blackjack, then the user loses (even if the user also has a blackjack).
    #  If the user gets a blackjack, then they win (unless the computer also has a blackjack).
    if winner:
        print("You win")
    else:
        print("you Lose")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while want_to_play == 'y':
    print(art.logo)
    user_deck = []
    computer_deck = []
    # TODO 1: Deal both user and computer a starting hand of 2 random card values.
    for _ in range(0, 2):
        user_deck = card_draw(cards, user_deck)
        computer_deck = card_draw(cards, computer_deck)

    # print(user_deck, computer_deck)

    if check_blackjack(computer_deck):
        print("You Lose")
    elif check_blackjack(user_deck):
        print("You Win")
    else:
        # TODO 5: If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
        replace_ace_value(user_deck)

    # TODO 6: Reveal computer's first card to the user.
    print(f"Your Cards: {user_deck}, current score: {deck_total(user_deck)}")
    print(f"Computer's first card: {computer_deck[0]}")

    # TODO 7: Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
    if check_blackjack(computer_deck):
        win_lose(False)
    elif check_blackjack(user_deck):
        win_lose(True)
    elif deck_total(user_deck) > 21:
        win_lose(False)

    want_to_continue = True
    while want_to_continue:
        # TODO 8: Ask the user if they want to get another card.
        user_choice = input("Type 'y' if you want to draw another card. Else 'n': ")
        if user_choice == 'y':
            want_to_continue = True
            user_deck = card_draw(cards, user_deck)
            replace_ace_value(user_deck)
            print(f"Your Cards: {user_deck}, current score: {deck_total(user_deck)}")
            if deck_total(user_deck) > 21:
                want_to_continue = False
        else:
            want_to_continue = False

    # TODO 9: Once the user is done and no longer wants to draw any more cards, let the computer play.
    #  The computer should keep drawing cards unless their score goes over 16.
    while deck_total(computer_deck) <= 16:
        computer_deck = card_draw(cards, computer_deck)

    # TODO 10: Compare user and computer scores and see if it's a win, loss, or draw.
    if deck_total(computer_deck) == 21:
        win_lose(False)
    elif deck_total(user_deck) == 21:
        win_lose(True)
    elif deck_total(user_deck) < 21:
        if deck_total(computer_deck) == deck_total(user_deck):
            print("Draw")
        elif deck_total(computer_deck) > deck_total(user_deck) and deck_total(computer_deck) < 21:
            win_lose(False)
        else:
            win_lose(True)
    else:
        win_lose(False)

    print(f"User's Deck: {user_deck}, total score: {deck_total(user_deck)}")
    print(f"Computer's Deck: {computer_deck}, total score: {deck_total(computer_deck)}")

    final_user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if final_user_choice == 'y':
        os.system('cls')
    else:
        want_to_play = 'n'
