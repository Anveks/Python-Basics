from tkinter import *

window = Tk()
window.title("My First GUI Programm")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# LABEL
my_label = Label(text="I am a label!", font=('Gothic', 24, 'bold'))
my_label.grid(column=0, row=0)

# INPUT
entry = Entry(width=10)
entry.grid(column=1, row=0)

# BUTTON
def button_click():
    my_label.config(text=entry.get())

button = Button(text='Click Me', command=button_click)
button.grid(column=2, row=0)

# SECOND BUTTON
button_2 = Button(text="I am a button.")
button_2.grid(column=2, row=0)

window.mainloop()
