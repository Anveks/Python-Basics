from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# PASSWORD GENERATOR #

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

password_list = password_letters + password_symbols + password_numbers

random.shuffle(password_list)

password = "".join(password_list)

# SAVE PASSWORD #
def save():
  site = site_input.get()
  email = email_input.get()
  password = password_input.get()
  
  if len(site) == 0 or len(email) == 0 or len(password) == 0: 
    messagebox.showerror(title='invalid input', message='All inputs should be complete.')
  else:
    # set the message box in a bool variable
    is_ok = messagebox.askokcancel(title=site, message=f'Are the details entered correct? \n\nEmail:{email}, \npassword: {password}')
    
    if is_ok:
      with open('./small projects/password-manager/data.txt', mode='a') as file:
        file.write(f'{site} | {email} | {password} \n\n')
        site_input.delete(0, END)
        password_input.delete(0, END)
        
def generate_password():
  password_input.delete(0, END)
  password_input.insert(0, password)
  pyperclip.copy(password) # automatically copying the password 

# UI SETUP #
window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50) 

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./small projects/password-manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# LABELS:
site_label = Label(text='Website:')
site_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# ENTRIES:
site_input = Entry(width=43)
site_input.grid(row=1, column=1, columnspan=2)
site_input.focus()
email_input = Entry(width=43)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'example@gmail.com')
password_input = Entry(width=25)
password_input.grid(row=3, column=1)

# BUTTONS:
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()