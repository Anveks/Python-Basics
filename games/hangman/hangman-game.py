import random
import words
import logo

print(logo.logo)

selected_word = words.word_list[random.randint(0, len(words.word_list) - 1)]
blank_word = []
tries = 6

for e in range(len(selected_word)):
    blank_word.append('_')

while tries != 0 and blank_word.count('_') != 0:
    guess = input('Guess a letter: \n').lower()

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



  
