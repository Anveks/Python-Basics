# Python Basics

Python is a versatile and widely-used programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is an interpreted, high-level language, meaning it is designed to be easy to understand and write code quickly.

### print() function

print() function simply prints everything inside the parenthesis in the console. Similar to console.log() in JS.

- accepts "" and '';
- \n - to create a new line;
- "+" to concat strings;

### input(promps) function

When executed it prints whatever is written inside the parenthesis and pauses the flow waiting for the user input data. Often used along with print(): 

      print("Hello " + input('What is your name?'))

## Python Variables

Obsiously you can store the data inside variables, like:

      name = input('What is your name? ')
      length = len(name)
      print(length)

We can store input values and override them as well:

      a = input("a: ") # 10
      b = input("b: ") # 5
      c = a # 10

      # switching the data:
      a = b
      b = c

      print(a, b) # 5 10

NB: usually, variables in Python are declared with '_': first_name, last_name etc. 

In Python, there is no built-in differentiation between constant variables and mutable variables. However, it is common convention in Python to use uppercase names for variables that are intended to be treated as constants. 

      # Constant variable (by convention):
      PI = 3.14159