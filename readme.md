# Python Basics

This tutorial is based on a few online courses and largely on Python documentation: https://docs.python.org/3/ .

AND askpython: https://www.askpython.com/ .

NB: An amazing site that visualizes code execution: https://pythontutor.com/ . Not only Python, also JS, C, Java, etc.

Python is a versatile and widely-used programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is an interpreted, high-level language, meaning it is designed to be easy to understand and write code quickly.

Table of Contents:
- [Indentation in Python](#indentation-in-python)
- - [print() function](#print-function)
- - [input(promps) function](#inputpromps-function)
- [Python Variables](#python-variables)
- [Python Data Types](#python-data-types)
- - [f-String](#f-string)
- [Conditional Statements](#conditional-statements)
- - [Randomisation in Python](#randomisation-in-python)
- [Python Lists](#python-lists)
- [For Loop](#for-loop)
- [Functions in Python](#functions-in-python)

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

## Python Tuple

A tuple is a type of data in Python. It is an ordered collection of elements, enclosed in parentheses (). It is similar to a list but has some key differences:

- Immutability
- Order
- Can store different data types
- Each element can be accessed by it index

```
            my_tuple = (1, 'hello', 3.14, True)

            print(my_tuple[0])  # Access the first element
            print(my_tuple[1])  # Access the second element
            print(my_tuple[-1])  # Access the last element

            # Slicing the tuple
            print(my_tuple[1:3])  # Slice from index 1 to 2 (exclusive)
```

So the most important thing about Tuples is that they are immutable; you cannot modify their elements. However, you can create a new tuple by concatenating or slicing existing tuples.

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

### Function Parameter vs Function Argument 

The terms "function parameter" and "function argument" are often used interchangeably, but they are actually two different things!

In Python and JavaScript:

- Function Parameter: A function parameter is a variable or placeholder declared in the function definition. It represents a value that the function expects to receive when it is called. Parameters are specified in the parentheses after the function name. For example, in Python:

```
            def greet(name):
                  print("Hello, " + name + "!")

                  greet("Alice")
```
Here 'name' is function parameter.

- Function Argument: A function argument is the actual value that is passed to a function when it is called. It is the value that gets assigned to the corresponding function parameter. In the example above, "Alice" is the argument passed to the greet function.

### Positional vs Keyword Arguments

In both Python and JavaScript, function arguments can be categorized as positional arguments or keyword arguments based on how they are passed to a function.

1. Positional Arguments:

- Positional arguments are arguments that are passed to a function based on their position or order.
- The order of the arguments in the function call must match the order of the parameters in the function definition.
- Positional arguments are commonly used when the function has a fixed number of parameters and the order of the arguments is important.

```
            def add(a, b):
                  return a + b

                  result = add(3, 5)
                  print(result)  # Output: 8
```
2. Keyword Arguments:

- Keyword arguments are arguments that are passed to a function using the parameter names as keywords.
- The order of the arguments does not matter when using keyword arguments.
- Keyword arguments are useful when a function has a large number of optional parameters or when you want to make the code more readable by explicitly specifying the arguments.


            def greet(name, age):
                  print("Hello, " + name + "! You are " + str(age) + " years old.")

                  greet(name="Alice", age=25)

JavaScript does not have built-in support for keyword arguments like Python. However, you can achieve a similar effect by passing an object and using its properties as named arguments.

            function greet(options) {
                  console.log("Hello, " + options.name + "! You are " + options.age + " years old.");
                  }

            greet({ name: "Alice", age: 25 });

## Dictionaries in Python

In Python, a dictionary is a built-in data structure that allows you to store and retrieve data in key-value pairs. It is also known as an associative array or a hash map in other programming languages.

In Python, dictionaries are defined using curly braces {} and use colons : to separate keys and values. Here's an example:

            person = {
                  "name": "John",
                  "age": 25,
                  "city": "New York"
                  }

You can access the values in a dictionary by using the keys as the index. For example:

            print(person["name"])  # Output: John
            print(person["age"])   # Output: 25
            print(person["city"])  # Output: New York

You can also modify the values in a dictionary or add new key-value pairs:

            person["age"] = 26  # Modifying the value of an existing key
            person["occupation"] = "Engineer"  # Adding a new key-value pair

And you can loop through the keys of a dictionary:

            for key in person:
                  print(key) # to log keys
                  print(person[key]) to log values

## Useful Modules:

Python offers a rich ecosystem of modules and packages that provide various functionalities for different purposes. Here are some commonly used and highly useful modules:

- os - Provides functions for interacting with the operating system, such as working with files and directories.
- sys - Offers system-specific parameters and functions, including system-level operations and command-line arguments.
- math - Provides mathematical operations and functions.
- random - Enables generation of random numbers, selections, and shuffling.
- datetime - Offers classes for manipulating dates, times, and time intervals.
- json - Allows encoding and decoding of JSON data.
- csv - Provides functionality for reading and writing CSV files.
- requests - Enables sending HTTP requests and interacting with web services.
- sqlite3 - Provides an interface to work with SQLite databases.
- logging - Offers a flexible logging system for recording events and messages during program execution.
- re - Provides regular expression matching operations for pattern searching and text manipulation.
- unittest - Offers a framework for writing and running unit tests.

## Docstrings in Python

In Python, a docstring is a string literal used to document modules, classes, functions, and methods. It serves as a documentation string that provides information about the object and its intended usage. Docstrings are enclosed in triple quotes (either single or double quotes) and are placed immediately after the definition of the object.

Here's an example of a docstring for a function:

```
            def greet(name):
                  """Greet a person by name.
                  
                  Args:
                        name (str): The name of the person to greet.
                  
                  Returns:
                        str: A greeting message with the person's name.
                  """
                  return f"Hello, {name}!"
```
Each time you want to use a function that has a docstring inside, a little documentation window will pop up showing you the text you've typed inside the docstring. 

## Notes on: While Loops, Flags and Recursion

In Python, a "flag" typically refers to a boolean variable that is used to control the flow of a program or indicate a certain condition or state. It is commonly used in conditional statements and loops to determine whether certain actions should be taken.

**Flags** are named after the concept of a flag used in real life, where a flag can be raised or lowered to indicate a specific signal or message. Similarly, in programming, a flag variable can be set or cleared to indicate a particular condition.

Flags can be used in various scenarios, such as controlling program flow, indicating the success or failure of an operation, or enabling/disabling certain functionality based on a condition. They provide a simple and effective way to control the behavior of a program.

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller subproblems. In the context of loops, recursion provides an alternative way to repeat a block of code.

A **while loop** is a control flow statement that repeatedly executes a block of code as long as a specified condition is true. It is used when you need to repeat a block of code an unknown number of times until a certain condition is met.

One of the good techniques from my own experience is to use recursion + while loops + boolean flags to control the code and achieve the needed results. See the *calculator.py* for more details.

## Local vs Global Scopes in Python:

In Python, variables can have either local or global scope, depending on where they are defined. The scope of a variable determines its visibility and accessibility throughout the program.

1. Local Scope:
- Variables defined within a function have local scope.
- They are accessible only within the function where they are defined.
- Local variables are created when the function is called and destroyed when the function completes execution.
- Local variables cannot be accessed from outside the function.

2. Global Scope:
- Variables defined outside any function or block have global scope.
- They are accessible throughout the entire program.
- Global variables are created when the program starts and destroyed when the program ends.
- Global variables can be accessed and modified from any part of the program.

Example for a global scope and 'global' keyword:

            x = 10  # Global variable

            def my_function():
             print(x)

            my_function()  # Output: 10
             print(x)  # Output: 10

            def another_function():
             global x  # Access the global variable
             x = 20
             print(x)

            another_function()  # Output: 20
             print(x)  # Output: 20

It's generally recommended to use local variables within functions to encapsulate and isolate the logic. However, when you need to modify a global variable from within a function, you can use the global keyword to indicate that you want to access the global variable instead of creating a new local variable with the same name.

Note: It's good practice to minimize the use of global variables and prefer passing arguments and returning values between functions to maintain code clarity and avoid unexpected side effects.

## Common Python Error Types:

1. SyntaxError: This error occurs when there is a mistake in the syntax of the Python code, such as missing parentheses, missing colons, or incorrect indentation.

2. NameError: This error occurs when you try to use a variable or function name that has not been defined or is not in the current scope.

3. TypeError: This error occurs when an operation or function is performed on an object of an inappropriate type. For example, trying to concatenate a string with an integer or calling a function that expects a certain type of argument with the wrong type.

4. IndexError: This error occurs when you try to access an element of a sequence (such as a list or string) using an invalid index, such as an index that is out of range.

5. ValueError: This error occurs when a function receives an argument of the correct type but with an invalid value. For example, passing a negative number to a function that expects a positive number.

6. KeyError: This error occurs when you try to access a dictionary using a key that does not exist in the dictionary.

7. AttributeError: This error occurs when you try to access an attribute or method of an object that does not exist.

8. IndentationError: This error occurs when there is a problem with the indentation of the code. Python relies on indentation to define the structure of the code, so incorrect or inconsistent indentation can lead to this error.

9. ImportError: This error occurs when you try to import a module that does not exist or cannot be found.

10. IOError: This error occurs when there is an input/output problem, such as trying to open a file that does not exist or is not accessible.

## OOP in Python: 💘

OOP stands for Object Oriented Programming. Before that the lead programming paradigm was PP: procedural programming.

**Procedural programming** is a programming paradigm that emphasizes the sequential execution of procedures or subroutines to solve a problem. It focuses on organizing code into reusable procedures or functions that perform specific tasks. PP is used in languages like COBOL (1959) or Fortran (1957).

In procedural programming, the focus is on writing procedures or functions that manipulate data, and the code is structured around these procedures. It is suitable for simpler programs or situations where data and functions are kept separate.

On the other hand,**OOP** focuses on creating objects that encapsulate data and behavior, allowing for more modular and reusable code. It is well-suited for complex systems, promotes code organization, and provides concepts like inheritance and polymorphism to facilitate code reuse and modularity.

**NB: Difference in syntax** - in JS we can create a new instance of a class by using the 'new' keyword; in Python you can do so simply by calling a class as if it was a function. 

### The Three Major OOP Concepts:

The three major concepts of object-oriented programming (OOP) are encapsulation, inheritance, and polymorphism. Here's a brief explanation of each concept:

1. **Encapsulation**: Encapsulation is the process of bundling data and methods (functions) together within a class, hiding the internal details and providing a public interface for interacting with the object. It ensures that data is accessed and modified through controlled methods, maintaining data integrity and preventing unauthorized access.

2. **Inheritance**: Inheritance is a mechanism that allows objects to inherit properties and behaviors from parent classes (superclasses) to child classes (subclasses). It promotes code reuse by enabling the creation of specialized classes that inherit and extend the attributes and methods of more general classes. Subclasses can add new features or modify existing ones while inheriting the common characteristics of the superclass.

3. **Polymorphism**: Polymorphism means the ability of objects to take on multiple forms. It allows objects of different classes to be treated as objects of a common superclass, enabling code to be written that can work with objects of different types. Polymorphism is achieved through method overriding and method overloading. It enhances code flexibility, modularity, and extensibility.

## Python Classes and their Syntax

Formation of a class with a class keyword, methods and attributes are pretty much the same in Python as they are in JavaScript, yet there are few differences in syntax:

1. Constructor:
Is the first function that is being called when you create a new instance of a class. In Python, it is represented by init function:

```
            class Person:
               def __init__(self, name, age):
                  self.name = name
                  self.age = age
```

2. "self": 
'self'  is the conventional name used as the first parameter in a method of a class (a constructor function is also a method!). It is a reference to the instance of the class on which the method is called. It is used to access instance variables and call other methods within the class. Same as 'this' in JavaScript.

3. Inheritance:
In JavaScript, if you want to create a class based on another class (inherit methods and attributes from it), you use the 'extends' keyword. While in Python the syntax runs as follows:

```
                  class BaseClass:
                        def __init__(self):
                              self.greeting = 'Hello!'
                        def greet(self):
                              print(self.greeting)

                  class DerivedClass(BaseClass):
                        def __init__(self):
                              super().__init__() # inherit the init function

                        def greet(self):
                              super().greet()  # inherit a custom method
```
NB: Don't forget about the super() function: the one that inherits all the methods and attributes from the parent-class stored inside the init() and ascribes them to the child-class.

### Small Note on Dot Notation in Python

Unlike in JS, in Python you cannot acces the values of a dictionary by using dot notation right away:

            my_dict = {'key1': 'value1', 'key2': 'value2'}

            print(my_dict.key1) # will throw an error

The right way to do it is by using **square brackets notation**:

            print(my_dict['key1'])

OR: the built-in get() method (because after all dictionaries are objects):

            print(my_dict.get('key1'))

Dot notation is typically used to access attributes of **objects** or **class** variables. There is of course a way to convert a dictionary into an object of a custom class, but generally it is not recommended.

In short: 
- JavaScript: allows both square bracket and dot notations with no differense whether it is an object or a class;
- Python: square notation for dictionaries, dot notation for objects and classes;

## Packages vs Modules

Basically each .py file you create is a module. Typically contains functions, classes and variables that you can use throughout your code by importing it here and there.

A **package** is a directory that contains multiple Python modules and an additional "init_.py" file - an empty file that contains initialization code for the package. 

To installa Python package in VSCode, open the project terminal and type:

            pip install *package-name*

Then you can import it anywhere as usual.

**The main site for Python packages:** https://pypi.org/ .

**NB**: The *requirements file* is not created automatically! To create one, you should open the terminal in project's directory and run:

            pip freeze > requirements.txt

This command will write all the installed package names and their versions to a file named requirements.txt in your current directory.


## Python Higher Order Functions and Event Listeners:

In Python, higher-order functions are functions that can take other functions as arguments or return functions as results. They enable functional programming paradigms and allow you to write more expressive and modular code.

Example:
```
            def add(a, b)
              return a + b

            def calc(a, b, add):
              return add(a, b)
```

Python provides several built-in higher-order functions such as map(), filter(), and reduce().

1. **filter()** function: It creates an iterator that filters out elements from an iterable based on a given function.

            numbers = [1, 2, 3, 4, 5]
            evens = list(filter(lambda x: x % 2 == 0, numbers))
            print(evens)  # Output: [2, 4]

2. **reduce()** function: It applies a rolling computation to a sequence of elements and returns a single value.

            from functools import reduce
            numbers = [1, 2, 3, 4, 5]
            product = reduce(lambda x, y: x * y, numbers)
            print(product)  # Output: 120

3. **map()** function: It applies a given function to each item in an iterable (e.g., a list) and returns an iterator of the results.

            numbers = [1, 2, 3, 4, 5]
            squared = list(map(lambda x: x ** 2, numbers))
            print(squared)  # Output: [1, 4, 9, 16, 25]

## Slicing Technique

In Python, slicing is a technique used to extract a portion (a slice) of a sequence, such as a string, list, or tuple. It allows you to extract a specific range of elements from the sequence by specifying the start index, end index, and step size.

Syntax:

            sequence[start:end:step]

Examples of usage:
```
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            letters = "Hello, World!"

            # Extract a range of elements from a list
            slice1 = numbers[2:6]  # [3, 4, 5, 6]
            slice2 = numbers[:5]   # [1, 2, 3, 4, 5]
            slice3 = numbers[5:]   # [6, 7, 8, 9, 10]
            slice4 = numbers[1:9:2]  # [2, 4, 6, 8]

            # Extract a range of characters from a string
            slice5 = letters[7:12]   # "World"
            slice6 = letters[::2]    # "Hlo ol!"
            slice7 = letters[::-1]   # "!dlroW ,olleH" # reverse a list

```

In addition to lists and strings, slicing can also be applied to **tuples** and other iterable objects that **support indexing**.

## Files, Directories and Paths in Python

You don't need any fs-libraries to read/write/append files in Python. There are two ways:

- Old way:

      file = open('my_file.txt')
      content = file.read()
      print(content)
      file.close()

NB: Closing the file after reading its contents is good practice because it releases the system resources associated with the file. 

- Using 'with' statement:

      with open('random_practices/my_file.txt', mode='r') as file: # mode = "read only"
      content = file.read()
      print(content)
      
      with open('random_practices/new_file.txt', mode='w') as file: # mode = 'write'
      file.write('My name is Darth Vader.')

In case of "with" statement, there is no need to close the file after using it - the file will be closed automatically.

## Absolute vs Relative Filepaths

Absolute and relative filepaths are two ways of to specify the location of a file in a file system.

An **absolute file path** provides the complete path starting from the root directory to the file. It includes all the directories and subdirectories necessary to locate the file. An absolute file path is independent of the current working directory. It typically starts with the root directory symbol (e.g., / in Unix-based systems or C:\ in Windows systems) and specifies all the directories and subdirectories leading to the file. For example: /home/user/documents/file.txt or C:\Users\user\Documents\file.txt.

A **relative file path** specifies the location of a file relative to the current working directory. It does not include the complete path from the root directory. Instead, it specifies the file's location in relation to the current working directory. Relative file paths are useful when you want to refer to files within the same directory or in directories relative to the current working directory. For example, if the current working directory is /home/user, a relative file path like documents/file.txt would refer to the file located at /home/user/documents/file.txt. Also, it is quite useful to use dots instead: ./ to specify the current folder, ../ to specify the parent folder of the current folder.

## Modules & Libraries to Work with Data

Since Python is often used in data analysis, there are many tools for working with different types of files and data that are either built-in or can be installed separately. For example, a CSV (Comma-Separated Values) module:

      import csv

      # Open the CSV file
      with open('data.csv', mode='r') as file:
      # Create a CSV reader object
      content = csv.reader(file)

      # Iterate over each row in the CSV file
      for row in content:
            # Access the data in each row
            print(row)

In this using the csv.reader method automatically converts the file into an object that we name 'content'; content is iterable, and each of its elements is presented as a list.

**Pandas library**: another very popular Python library for data manipulation and analysis.

      pip install pandas

Documentation: https://pandas.pydata.org/docs/

      import pandas

      data = pandas.read_csv('data.csv')

The data will be represented as a table. It is possible to access the table values simpy by defining the name of the column.

Pandas provides two primary data structures: *Series* and *DataFrame*: 
- Series is a one-dimensional labeled array capable of holding any data type; 
- DataFrame is a two-dimensional table-like data structure with columns of potentially different data types.

## List Comprehension 

List comprehension is a unique feature of Python. It is the ultimate 'one-liner':

      new_list = [for item in list]

What we do here is  creating a new list **by iterating** over an existing iterable (such as a list, tuple, or string). It is also possible to apply expressions or conditions to each element! Example:

      list = [0,1,2]
      new_list = [item + 1 for item in list] # Output: [1,2,3]

Conditions:

      list = [2,4,5]
      new_list = [item for item in list if item % 2 == 0]

## Dictionary Comprehension

Same as list comprehension but with dictionaries: allows you to create dictionaries by specifying key-value pairs using a compact syntax. Here's the general syntax for dictionary comprehension. Example:

      student_names = {'Dave', 'Tom', 'John', 'Lucas'}
      student_grades = { student: random.randint(1, 100) for student in student_names }

Example for creating a new dictionary with a condition:

      student_names = {'Dave', 'Tom', 'John', 'Lucas', 'Alice', 'Jake', 'Dean', 'Sam', 'Caroline', 'Jane', 'Matthew', 'Chloe'}
      student_grades = { student: random.randint(1, 100) for student in student_names }
      passed_students = { student:grade for (student, grade) in student_grades.items() if grade >= 60 }

## Tkinter and GUI

Tkinter is a built-in Python module for creating graphical user interfaces (GUIs). It provides a set of tools and widgets to create windows, buttons, labels, input fields, and other GUI elements. Tkinter is widely used and comes pre-installed with Python, making it easily accessible for creating desktop applications with a graphical interface.

      import tkinter

      window = tkinter.Tk()
      window.title('My First GUI Programm')

      window.mainloop() # there is a built-in while loop inside

You can create components and place them inside the window like this:

      my_label = tkinter.Label(text="I am a label!", font=('Gothic', 24, 'bold'))
      my_label.pack() # this method places the label inside the window

## *args and **kwargs 

In Python, *args and **kwargs are used in function definitions to allow the function to accept a variable number of arguments.

- The *args syntax allows you to pass a variable number of non-keyword arguments to a function. The *args parameter inside a function definition gathers all the non-keyword arguments into a tuple, which can then be accessed within the function. The name args is a convention, but you can use any valid variable name with the * prefix.

**NB**: there is a similar concept in JavaScript called the 'rest parameter': it allows a function to accept an indefinite number of arguments as an array. 

- The **kwargs stands for 'key word arguments' and it is only different from the *args because it allows us to pass a variable number of *keyword arguments* to a function. It gathers all the parameters into a dictionary where the keys are argument names and the values are argument values. 

            def print_info(**kwargs):
                  for key, value in kwargs.items():
                        print(f"{key}: {value}")

                  print_info(name="John", age=30, occupation="Engineer")
                  # Output:{'name': 'John', 'age': 30, 'occupation': 'Engineer'}

A more vivid example of **kwargs:

            def calc(n, **kwargs)
                  print(kwargs)
                  n += kwargs['add']
                  n *= kwargs['multiply']
                  print('n')
            calc(2, add=2, multiply=3)
