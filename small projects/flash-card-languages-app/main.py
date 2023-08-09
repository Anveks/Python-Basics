from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# FUNCTIONS

def generate_word():
  data = pandas.read_csv(r"small projects\flash-card-languages-app\data\french_words.csv")
  data_dict = data.to_dict()
  random_index = random.randint(0,100)
  random_word = data_dict['French'][random_index]
  flash_card.itemconfig(word, text=random_word)

# UI SETTINGS
window = Tk()
window.title('Flashies')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#  images:
RIGHT_IMG = PhotoImage(file='./small projects/flash-card-languages-app/images/right.png')
WRONG_IMG = PhotoImage(file='./small projects/flash-card-languages-app/images/wrong.png')
CARD_IMG_FRONT = PhotoImage(file=r".\small projects\flash-card-languages-app\images\card_front.png")
CARD_IMG_BACK = PhotoImage(file=r".\small projects\flash-card-languages-app\images\card_back.png")

flash_card = Canvas(width=800, height=526)
flash_card.create_image(400, 263, image=CARD_IMG_FRONT)
flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.grid(row=0, column=0, columnspan=2)

title = flash_card.create_text(400, 130, text='Title', font=( 'Ariel', 40, 'italic' ))
word = flash_card.create_text(400, 243, text='word', font=( 'Ariel', 60, 'bold' ))

known_button = Button(window, image=RIGHT_IMG, highlightthickness=0, command=generate_word)
known_button.grid(row=1, column=1)
unknown_button = Button(window, image=WRONG_IMG, highlightthickness=0, command=generate_word)
unknown_button.grid(row=1, column=0)

window.mainloop()
