
print("Welcome to the Simple Word Game")

direction = input('You have arrived on an island. You see a path. Should you take it left or right? \n').lower()

if direction == 'left':
    print('You have walked a lot and now you see a lake in front of you.')
    action = input('Will you swim or wait? \n').lower()
    
    if (action == 'wait'):
        print('You have waited and suddenly three doors started to appear: red, blue and yellow.')
        color = input('Which color will you choose? \n').lower()

        if (color == 'blue') or (color == 'red'):
            print('Game over!')
        else:
            print('You have found the treasure! 🪙')

    else:
        print('Oops! Game over. ☠️')   
else:
    print('Oops! Game over.')    
