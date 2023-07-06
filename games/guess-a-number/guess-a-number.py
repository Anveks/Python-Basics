import random
import os

difficulty = input('Select a difficulty level: type "easy" or "hard". \n').lower()
game_over = False

def play_game():
    tries = 0
    secret_number = random.randint(1, 101)
    number = 0

    if difficulty == 'easy':
        tries = 10
    if difficulty == 'hard':
        tries = 5

    while tries != 0 and number != secret_number:
        number = int(input('Guess a number: \n'))

        if number < secret_number:
            print('Too low!')
        elif number > secret_number:
            print('Too high!')

        tries -= 1
        if tries != 0:
          print(f"You have {tries} tries left.")

    if number == secret_number:
        return 'won'
    elif tries == 0:
        print(f'The secret number was: {secret_number}')
        return 'lost'

if play_game() == 'won':
    game_over = True
    print('You won! 🎉')
else:
    game_over = True
    print('You lost! ☠️')

try_again = input('Try again? Yes or no. \n').lower()
if try_again == 'yes':
    game_over = False
    play_game()
else:
    os.system('cls')
    print('Bye bye! 👋')
