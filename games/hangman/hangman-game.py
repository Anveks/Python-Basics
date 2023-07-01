import random
import words
import logo

print(logo.logo) # adding a logo

selected_word = words.word_list[random.randint(0, len(words.word_list) - 1)] # picking a random word
blank_word = [] # preparing an empty list
tries = 6 # number of tries is standard

for _ in range(len(selected_word)): # filling the blank list with dashes of the same number with selected word
    blank_word.append('_')

while tries != 0 and blank_word.count('_') != 0: # defining the condition: untill tries are not zero and there are still dashes in the blank_word
    guess = input('Guess a letter: \n').lower()

    if guess in blank_word:
        print(f'You have already guessed this letter.')

    for i in range(0, len(selected_word)):
        letter = selected_word[i]
        if letter == guess:
            blank_word[i] = letter
            print(blank_word)
            if blank_word.count('_') == 0:
                print('You won! 🎉')
                break   
        
    if guess not in selected_word:
        tries -= 1
        print(f'Wrong guess! Tries left: {tries}')
        if tries == 0:
            print(f'You lost! ☠️ The word was: {selected_word}.')



  
