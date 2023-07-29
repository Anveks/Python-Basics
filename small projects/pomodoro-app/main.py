from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# TIMER RESET # 

# TIMER MECHANISM # 

# COUNTDOWN MECHANISM # 

# UI SETUP #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW) # setting the paddings

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./small projects/pomodoro-app/tomato.png") # we store the img
canvas.create_image(100, 112, image=tomato_image) # first we specify the height and width

def start():
  pass

def reset():
  pass

start_button = Button(window, text='start', command=start)
reset_button = Button(window, text='reset', command=reset)
title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font={FONT_NAME, 50})

canvas.create_text(100, 130, text='00:00', fill='white', font={FONT_NAME, 35, 'bold'})

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)

window.mainloop()

