import turtle
from prettytable import PrettyTable

# turtle is a built-in class in python created for educational purposes: https://docs.python.org/3/library/turtle.html

# assaf = turtle.Turtle()
# print(assaf)
# assaf.shape('turtle')
# assaf.color('green')
# assaf.forward(100)

# my_screen = turtle.Screen() # this will create a window with a small screen with a turtle in it
# print(my_screen.canvheight) # check the height of the screen: 300 px
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Element", ['Electricity', 'Water', 'Fire'])
table.align = 'l'
print(table)