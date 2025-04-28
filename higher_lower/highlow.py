from game_data import data
from art import logo
import random
LOGO = logo
DATA = data
#TODO 1:import the data required
#TODO 2:select the random account name from the dictionary
#TODO 3:ask the user to select if the second account has more or less followers
#TODO 4: compare the amount of followers and check the user's selection
def game_on(score):
    def start(account1, account2):
        acct1_name = account1['name']
        acct2_name = account2['name']
        #print(f'{account1["follower_count"]} vrs {account2["follower_count"]}')
        guess = input(f'Enter if {acct1_name} has Higher or Lower amount of followers than {acct2_name}:  ').lower()
        result = compare(account1,account2)
        if result == guess or result == 'tie':
            win = True
        else:
            win = False
        return win
    def select_account():
        #gets a dictionary from the list of dictionaries and selects the account
        account = random.choice(DATA)
        return account
    def compare(account1, account2):
        if account1['follower_count'] < account2['follower_count']:
            return 'lower'
        elif account1['follower_count'] > account2['follower_count']:
            return 'higher'
        elif account1['follower_count'] == account2['follower_count']:
            return 'tie'
    def info():
        print(f'{acct1["name"]} has {acct1["follower_count"]} on Instagram')
        print(f'{acct2["name"]} has {acct2["follower_count"]} on Instagram')

    #TODO 5: if the user is correct, keep the account as the first account and randomly pick a second account
    print(LOGO)
    acct1 = select_account()
    acct2 = select_account()
    victory = start(acct1,acct2)
    while victory:
        print("YOUR ANSWER IS CORRECT!")
        score += 1
        info()
        acct1 = acct2
        acct2 = select_account()
        victory = start(acct1,acct2)
    print("OH NO... YOU LOST!")
    print(f'Your score is {score}')
    info()
    play_again = input("Would you like to play again? (Y/N) ").lower()
    return play_again

play = True
score = 0
while play:
    next = game_on(score)
    if next == 'y':
        play = True
    else:
        play = False
