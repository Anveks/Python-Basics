import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def getCard():
    return cards[random.randint(0, len(cards) - 1)]

user = [getCard(), getCard()]
computer = [getCard(), getCard()]

user_won = False
computer_won = False

def checkScore(player, score): 
    global user_won
    global computer_won

    total_score = sum(score)
    print(f"{player} score is: {total_score}")

    if player == 'user' and total_score == 21:
        user_won = True
    elif player == 'computer' and total_score == 21:
        computer_won = True

    if total_score > 21:
        if 11 not in score:
            if player == 'user':
                computer_won = True
            elif player == 'computer':
                user_won = True
        else:
            score[score.index(11)] = 1
            new_total_score = sum(score)
            if new_total_score > 21:
                if player == 'user':
                    computer_won = True
                elif player == 'computer':
                    user_won = True
            else:
                choice = input('Do you want to try another card? Yes or no.\n').lower()
                if choice == 'yes':
                  user.append(getCard())
                  checkScore('user', user)
                else:
                 computer.append(getCard())
                 checkScore('computer', computer)
    else:
      choice = input('Do you want to try another card? Yes or no.\n').lower()
      if choice == 'yes':
        user.append(getCard())
        checkScore('user', user)
      else:
        computer.append(getCard())
        checkScore('computer', computer)                  

checkScore('user', user)
checkScore('computer', computer)

if user_won:
    print('User won! 🎉')
elif computer_won:
    print('Computer won! 🔥')
elif sum(user) == 21 and sum(computer) == 21:
    print('It\'s a draw! Both player and computer have blackjack!')
elif sum(user) == 21:
    print('User won! 🎉')
elif sum(computer) == 21:
    print('Computer won! 🔥')
else:
    print('No one wins. It\'s a draw!')
