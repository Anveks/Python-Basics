# Python Basics

This tutorial is based on a few online courses and largely on Python documentation: https://docs.python.org/3/ .

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

## Python Data Types

You can check each variable's datatype by type() method.

It is possible to convert variables to different datatypes like str(100)/float("123")/int(12.5).

Python is very type-sensitive so for example this:

      age = 12
      print("you are " + age + "years old")

Will return a TypeError because we cannot concatenate strings with numbers. Unlike in JS where 12 will be automatically converted in a string after seeing a + operator.      

1. Numeric types:
int: age = 25
float: pi = 3.14
complex: z = 2 + 3j

You can round the math result by using round(); also double division would help: //. 

Shorter syntax like a += a would be the same as a = a + a.

2. Boolean type:
bool: is_true = True
bool: is_false = False

3. String type:
str: name = "John Doe"
str: message = 'Hello, World!'

You can access a specific char of a string by using its index: print("abc"[0]) will return 'a'.

You can check the length of a string by using the len() method. 

4. Container types:
- List: numbers = [1, 2, 3, 4, 5]
- Tuple: coordinates = (10, 20)
- Set: fruits = {'apple', 'banana', 'orange'}
- Dictionary: person = {'name': 'Alice', 'age': 30}

5. None type:
None: result = None

### f-String

An f-string, short for "formatted string literal," is a feature introduced in Python 3.6 that provides a concise and convenient way to embed expressions inside string literals. It allows you to interpolate variables, expressions, and even function calls directly into strings by prefixing the string with the letter "f" or "F" and enclosing the expressions within curly braces {}.

      name = "Alice"
      age = 30

      # Using f-string to create a formatted string
      message = f"Hello, my name is {name} and I am {age} years old."

      print(message)

In JavaScript, a similar feature to Python's f-strings is called "template literals" or "template strings." Template literals allow you to embed expressions and variables within backtick (``) delimited strings.

## Conditional Statements  

Basically the same as they are in JS.

1. if statement: 
The if statement is used to execute a block of code if a specified condition is true.

2. if-else statement: 
The if-else statement is used to execute one block of code if the condition is true and another block of code if the condition is false.

3. if-elif-else statement: 
The if-elif-else statement allows you to test multiple conditions and execute different blocks of code based on the first condition that evaluates to true.

4. nested if statements: 
You can also nest conditional statements within each other to create more complex conditions.

```
      x = 10
      y = 5

      if x > 5:
          if y > 2:
              print("x is greater than 5 and y is greater than 2")
          else:
              print("x is greater than 5 but y is not greater than 2")
      else:
          print("x is not greater than 5")
```

NB: Pay attention to spaces tabs and indentation in general because Python is extremely indentation-sensitive! There is even a special type of errors: IndentationError.

Comparison operators are the same as they are in JS. = goes for asssignment, == checks equality. 