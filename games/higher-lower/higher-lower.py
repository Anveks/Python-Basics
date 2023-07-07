import data
import random
import os

print('Welcome to the higher-lower game. \nThe rules are simple: you get two Instagram accounts and you are to guess who has more followers. 📸')

GAME_DATA = data.data

# function that returns a random elem from the game data list:
def get_random_account():
    return random.choice(GAME_DATA)

def play_game():
    score = 0
    game_over = False
    bigger_account = {}

    # while game is not over - run this code in a loop:
    while not game_over:
        account_a = {}
        account_b = get_random_account()

        if bigger_account != {}: # in case bigger_account is not empty = assign it to acc_a
            account_a = bigger_account
        else: # if it is empty - get a random element
            account_a = get_random_account()

        if account_a['name'] == account_b['name']: # duplication filter
            account_a = get_random_account()

        biggest = '' # biggest account as 'A' or 'B'

        if account_a['follower_count'] > account_b['follower_count']:
            biggest = 'A'
            bigger_account = account_a
        else:
            biggest = 'B'
            bigger_account = account_b

        choice = input(f"Who has more followers? \n{account_a['name']}: a {account_a['description'].lower()} from {account_a['country']}, or {account_b['name']}: a {account_b['description'].lower()} from {account_b['country']}. Type 'A' or 'B': \n").upper()

        if choice == biggest: # in case there is a match:
            os.system('cls') # clear the terminal
            print('That\'s correct!')
            score += 1 # add score
            print(f'Your score is: {score}')
            account_b = get_random_account() # get new random acc_b (acc_a is the biggest_acc)
        else:
            print('Game over!')
            print(f'Your score was: {score}')
            game_over = True # in case of mismatch - exit the loop

play_again = 'yes' # default

while play_again == 'yes':
    os.system('cls')
    play_game() # in case the loop inside this function gets destroyed, continue to the next input
    play_again = input('Play again? (yes/no): ').lower() # if 'yes' - run the loop again, 'no' - exit

print('Bye bye! 👋') # final message after the loop is destroyed
