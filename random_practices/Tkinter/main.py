import tkinter

window = tkinter.Tk()
window.title("My First GUI Programm")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label!", font=('Gothic', 24, 'bold'))
my_label.pack()


window.mainloop()