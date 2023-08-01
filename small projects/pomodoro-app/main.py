from tkinter import *
import time
import math
# CONSTANTS #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# TIMER RESET # 
def reset():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text='00:00')
  title_label.config(text='Timer')
  check_marks.config(text="")
  global reps
  reps = 0

# TIMER MECHANISM # 
def start():
  global reps
  reps += 1
  
  if reps % 2 != 0:
    count_down(WORK_MIN * 60)
    title_label.config(text='Work', fg=GREEN)
    open_popup('Time to work!')
  elif reps % 2 == 0:
    count_down(SHORT_BREAK_MIN * 60)
    title_label.config(text='Short Break', fg=PINK)
    open_popup('Time for a break!')
  elif reps % 8 == 0:
    count_down(LONG_BREAK_MIN * 60)
    title_label.config(text='Long Break', fg=RED)
    open_popup('Time for a break!')
    
# POPUP WINDOW
def open_popup(text):
   top = Toplevel(window)
   top.geometry("350x250")
   top.title("Child Window")
   Label(top, text=text, font=('Mistral 18 bold')).place(x=150,y=80)

# COUNTDOWN MECHANISM # 
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  
  canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
  if count > 0: 
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start()
    marks = ""
    times = math.floor(reps / 2)
    for _ in range(times):
      marks += '✔'
      
    check_marks.config(text=marks)

# UI SETUP #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW) # setting the paddings

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./small projects/pomodoro-app/tomato.png") # we store the img
canvas.create_image(100, 112, image=tomato_image) # first we specify the height and width
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font={FONT_NAME, 35, 'bold'})

start_button = Button(window, text='start', command=start, highlightthickness=0)
reset_button = Button(window, text='reset', command=reset, highlightthickness=0)
title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font={FONT_NAME, 50})
check_marks = Label(bg=YELLOW, fg=GREEN)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
check_marks.grid(column=1, row=3)

window.mainloop()

