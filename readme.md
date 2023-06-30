# Python Basics

This tutorial is based on a few online courses and largely on Python documentation: https://docs.python.org/3/ .

AND askpython: https://www.askpython.com/ .

Python is a versatile and widely-used programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is an interpreted, high-level language, meaning it is designed to be easy to understand and write code quickly.

Table of Contents:
   1.1. [Indentation in Python](#indentation-in-python)
      1.1.1. [print() function](#print-function)
      1.1.2. [input(promps) function](#inputpromps-function)
   1.2. [Python Variables](#python-variables)
   1.3. [Python Data Types](#python-data-types)
      1.3.1. [f-String](#f-string)
   1.4. [Conditional Statements](#conditional-statements)
   1.5. [Randomisation in Python](#randomisation-in-python)
   1.6. [Python Lists](#python-lists)
   1.7. [For Loop](#for-loop)
   1.8. [Functions in Python](#functions-in-python)

## Indentation in Python

In Python, indentation plays a crucial role in defining the structure and hierarchy of the code. Unlike many other programming languages that use curly braces or keywords to denote code blocks, Python uses indentation to indicate the grouping of statements.

Indentation refers to the spaces or tabs placed at the beginning of a line to position the code relative to the surrounding blocks. It is used to define the scope of control structures (such as loops and conditionals) and the body of functions, classes, and other code blocks.

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

Will return a TypeError because we cannot concatenate strings with numbers. Unlike in JS where 12 will be automatically converted in a string after a + operator.      

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

## Randomisation in Python

Randomization in Python refers to the generation of random values or the shuffling of existing data. The random module in Python provides functions and methods for working with random numbers and randomness. It uses various mechanisms to generate random values.

Python's random module uses a pseudorandom number generator (PRNG) to generate random numbers. PRNGs are algorithms that produce sequences of numbers that appear to be random but are actually deterministic. The random module uses the Mersenne Twister algorithm, which is a widely-used PRNG, to generate random numbers.

An article about Mersenne Twister: https://en.wikipedia.org/wiki/Mersenne_Twister .

Basically what you need to do is to import a buil-in random module:

      import random

And then use it's methods to create random numbers:

      random_integer = random.randint(1, 10)

For floats:

      random_float: random.random()

for decimals:

      from decimal import Decimal

      num1 = Decimal('0.1')

## Python Lists

One of the container datatypes existing in Python. Is really similar to an Array in JS.

Similarities:

- Indexed Access: Both Python lists and JS arrays allow access to individual elements using their index. The indexing starts from 0.
- Mixed Data Types: Both Python lists and JS arrays can contain elements of different data types, including numbers, strings, objects, and even other lists or arrays.
- Dynamic Size: Both Python lists and JS arrays can change in size dynamically. Elements can be added or removed from the collection.

Differences:

- Syntax: The syntax for defining and working with lists and arrays differs between Python and JS. In Python, lists are enclosed in square brackets ([]), while in JS, arrays are defined using square brackets ([]) or the Array constructor.
- Flexible Length: Python lists can have a flexible length, meaning they can contain a different number of elements at different points in time. In JS, arrays are also flexible in length, and the length can change dynamically.
- Built-in Methods and Functions: Python lists and JS arrays have different built-in methods and functions available for manipulating and working with them. The specific methods and functions provided differ between the two languages.
- Underlying Implementation: Internally, Python lists and JS arrays are implemented differently. Python lists are implemented as dynamic arrays, while JS arrays can be implemented as sparse arrays or dynamic objects.

You can modify an element of a List by acessing it with its index:

            list = [a, b, c]
            list[0] = d

You can also add new List inside:

            list.extend([f, g]) // this will be added 

OR:

            list.insert("x") // for adding single elements

And to delete an element:

            list.pop(1) // stating the index
            list.remove(1) // does the same

            del list[1] // will delete the first element

## For Loop 

In Python, you can use a for loop to iterate over a sequence of elements such as a list, tuple, string, or range. The basic syntax of a for loop in Python is as follows:

            for item in sequence:
                  # Code block to be executed for each item

You can also combine a for loop with other control flow statements, such as if statements, to perform conditional operations or control the flow of execution within the loop. Additionally, you can use the range() function to generate a sequence of numbers and iterate over it using a for loop.

            list = [1,2,3]
            for num in range([start], [stop], [step]):
                  print(num)

start will be the starting index
stop will be the whole length
step will be specification of an increment

In JS:

            for (i = 0; i < arr.length; i++){
                  console.log(arr[i])
            }

## While Loop

As in JS, allows you to repeatedly execute a block of code as long as a specified condition is true. The general syntax of a while loop in Python is as follows:

```
            while condition:
                  # Code block to be executed
```

It's important to ensure that the condition within the while loop eventually becomes false; otherwise, the loop will continue indefinitely, resulting in an infinite loop. To avoid infinite loops, make sure to include code within the loop that can modify the condition or break out of the loop when necessary.

Here's an example that demonstrates how to exit a while loop using a break statement:

            count = 1
            while True:
                  print(count)
                  count += 1
                  if count > 5:
                        break

The main difference between a for loop and a while loop is that a for loop is used for iterating over a known sequence, while a while loop is used for executing a block of code repeatedly as long as a specified condition is true.\

NB: Be aware of intinite loops! That's why while loops are less preferable in coding than for loops.

## Functions in Python

Here's the syntax for defining a function in Python:

```
            def function_name(parameters):
                  # Function body
                  # Code block
                  # Statements

                  # Optional: return statement
                  return value
```

def: a keyword that indicates the start of a function definition.

NB: ALWAYS be careful with the indentation. 

### NOT IN Operator

In Python, the keyword not in is a logical operator used to check if a value does not exist in a sequence, such as a string, list, or tuple. It is the negation of the in operator.

Here's the syntax:

```
            fruits = ['apple', 'banana', 'orange']

            # Check if 'mango' is not in the list
            if 'mango' not in fruits:
            print("Mango is not in the list.")

            # Check if 'banana' is not in the list
            if 'banana' not in fruits:
            print("Banana is not in the list.")
            else:
            print("Banana is in the list.")
```