import random
import os

game_over = False # stating a boolean flag for while loop

# the one and the only function:
def play_game():
    difficulty = input('Select a difficulty level: type "easy" or "hard". \n').lower()

    tries = 0
    secret_number = random.randint(1, 101) # 101 'cause the last int of a range always omitted
    number = 0

    if difficulty == 'easy':
        tries = 10
    elif difficulty == 'hard':
        tries = 5
    else: return

    # while the user still has tries and hasn't guessed the number yet: continue the loop
    while tries != 0 and number != secret_number:
        number = int(input('Guess a number: \n'))

        if number < secret_number:
            print('Too low!')
        elif number > secret_number:
            print('Too high!')

        tries -= 1
        if tries != 0:
            print(f"You have {tries} tries left.")

    # if the user guessed the number, return 'won' and exit the function
    if number == secret_number:
        return 'won'
    # if the user doesnt have any tries left - return 'lost' and exit the function
    elif tries == 0:
        print(f'The secret number was: {secret_number}')
        return 'lost'

# while the boolean flag we stated at the beginning is not true - continue the loop
while not game_over:
    # this is the first time we call the play_game() function and the starting point:
    result = play_game()

    if result == 'won':
        print('You won! 🎉')
    elif result == 'lost':
        print('You lost! ☠️')
    else: print('Somthing went wrong...')

    try_again = input('Try again? Yes or no. \n').lower()
    if try_again == 'no':
        print('Bye bye! 👋')
        game_over = True
    else:
        os.system('cls')
