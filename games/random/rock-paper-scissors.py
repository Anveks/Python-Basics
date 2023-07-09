import random 

rpc = ['rock', 'paper', 'scissors']

player_turn = input('Rock paper or scissors? Pick one: \n')
computer_turn = rpc[random.randint(0, len(rpc) - 1)]

print(computer_turn)

if player_turn == 'rock' and computer_turn == 'paper':
    print('Computer won!')
elif player_turn == 'rock' and computer_turn == 'rock':
    print('Its a draw!')
elif player_turn == 'rock' and computer_turn == 'scissors':
    print('You won!')
elif player_turn == 'paper' and computer_turn == 'scissors':
    print('Computer won!')
elif player_turn == 'paper' and computer_turn == 'paper':
    print('Its a draw!')
elif player_turn == 'paper' and computer_turn == 'rock':
    print('You won!')
elif player_turn == 'scissors' and computer_turn == 'rock':
    print('Computer won!')
elif player_turn == 'scissors' and computer_turn == 'scissors':
    print('Its a draw!')
elif player_turn == 'scissors' and computer_turn == 'paper':
    print('You won!')
else:
    print('Something went wrong... Try running the programm once again.')

#  the same but with Dictionary instead of a List: 

import random

rpc = ['rock', 'paper', 'scissors']
player_turn = input('Rock, paper, or scissors? Pick one: \n')
computer_turn = random.choice(rpc)

print(computer_turn)

outcomes = {
    'rock': {'rock': "It's a draw!", 'paper': 'Computer won!', 'scissors': 'You won!'},
    'paper': {'rock': 'You won!', 'paper': "It's a draw!", 'scissors': 'Computer won!'},
    'scissors': {'rock': 'Computer won!', 'paper': 'You won!', 'scissors': "It's a draw!"}
}

if player_turn in outcomes and computer_turn in outcomes[player_turn]:
    print(outcomes[player_turn][computer_turn])
else:
    print('Something went wrong... Try running the program again.')
