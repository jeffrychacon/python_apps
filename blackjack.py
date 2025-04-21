import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def scores(hand):
    return sum(hand)

def ace_replacement(any_hand):
    which_ace = any_hand.index(11)
    print(which_ace)
    any_hand[which_ace] = 1
    return any_hand
def play(hand):
    hand.append(random.choice(cards))
    return hand
def winner(computer_hand,user_hand):
    user_total = scores(user_hand)
    computer_total = scores(computer_hand)
    #To process the ace replacement
    if computer_total > 21 and 11 in computer_hand:
        ace_replacement(computer_hand)
        winner(computer_hand, user_hand)
    if user_total > 21 and 11 in user_hand:
        ace_replacement(user_hand)
        winner(computer_hand, user_hand)
    if computer_total == 21:
        blackjack = "Computer"
    elif user_total == 21 :
        blackjack = "Player"
    elif computer_total > user_total and computer_total < 21:
        blackjack = "Computer"
    elif user_total > computer_total and user_total < 21:
        blackjack = "Player"
    elif user_total < computer_total and computer_total > 21:
        blackjack = "Player"
    elif user_total > 21:
        blackjack = "Computer"
    else:
        blackjack = "Draw"
    return blackjack

gameon = 'y'
while gameon == 'y':
    user_hand = [random.choice(cards), random.choice(cards)]
    # user_hand = [11,11]
    computer_hand = [random.choice(cards), random.choice(cards)]
    # computer_hand = [11,11]
    print("****** Cards ******")
    print(f"Computer's cards: [{computer_hand[0]}, X]")
    print(f"Player's cards: {user_hand}")
    another_card = input("Do you want another card? y/n ")
    while another_card == 'y':
        play(user_hand)
        print(f"Player's cards: {user_hand}")
        if scores(user_hand) > 21:
            who_wins = winner(computer_hand,user_hand)
            break
        print("Its the computer's turn")
        if scores(computer_hand) <= 16:
            play(computer_hand)
            print("Computer played")
            if scores(computer_hand) == 21:
                who_wins = winner(computer_hand, user_hand)
                break
        another_card = input("Do you want another card? y/n ")
    print(f"Computer's cards: {computer_hand}")
    who_wins = winner(computer_hand,user_hand)
    print(f"The winner is the {who_wins}")
    print("****** Scores ******")
    print(f"The computer score is {scores(computer_hand)}")
    print(f"The player score is {scores(user_hand)}")
    gameon = input(f"Would you like to play again? y/n ")