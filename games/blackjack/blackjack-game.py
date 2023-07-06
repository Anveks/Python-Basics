import random
import os

# generate a random card
def get_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0, len(cards) - 1)]

# calculate the score:
def calculate_score(cards):
  # in case it is blackjack return 0:
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # in case the sum is more then 21 and there is an ace:
  if 11 in cards and sum(cards) > 21:
    cards[cards.index(11)] = 1
    return int(sum(cards))
  # else return the sum:
  return sum(cards)

# check the winner
def compare_scores(user_score, computer_score):
  if user_score == computer_score: return ' It\'s a draw!'
  elif computer_score == 0: return '  Computer won!'
  elif user_score == 0: return '  You won!'
  elif computer_score > 21: return '  You won! Computer went over 21.'
  elif user_score > 21: return '  Computer won! You went over 21.'
  elif user_score > computer_score: return '  You won!'
  else: return '  You lose!'

def play_game():
  end_game = False # that is a flag for the while loop

  user_cards = [get_cards(), get_cards()] # get random user_cards and computer_cards
  computer_cards = [get_cards(), get_cards()]

  while end_game == False: # continue the loop untill its end_game
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f'Your cards: {user_cards}, your score: {user_score}')
    print(f'Computer first card: {computer_cards[0]}')

    if user_score == 0 or computer_score == 0 or user_score > 21: # if blackjack - end game
      end_game = True
    else: # if no blackjack and sum is not exceening 21
      choice = input('Do you want to try another card? Yes or no.\n').lower()
      if choice == 'yes': # get a new card
        user_cards.append(get_cards())
      else: # skip a new card and get to computer's while loop:
        end_game = True

  # computer's while loop:
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(get_cards())
    computer_score = calculate_score(computer_cards)

  # after all while loops are closed, we call the compare_scores function:
  print(f'Your cards: {user_cards}, your score: {user_score}')
  print(f'Computer cards: {computer_cards}, computer score: {computer_score}')
  print(compare_scores(user_score, computer_score))

# the first thing the user sees is this input:
while input('Do you want to play a game? \n').lower() == 'yes':
  os.system('cls')
  play_game()
