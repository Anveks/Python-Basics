import turtle
from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column("Element", ['Electricity', 'Water', 'Fire'])
# table.align = 'l'
# print(table)

# turtle is a built-in class in python created for educational purposes: https://docs.python.org/3/library/turtle.html

assaf = turtle.Turtle()
assaf.shape('turtle')
assaf.color('green')

def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    assaf.forward(100)
    assaf.right(angle)

for shape_side_n in range(3, 11):
  draw_shape(shape_side_n)
  
my_screen = turtle.Screen() # this will create a window with a small screen with a turtle in it
print(my_screen.canvheight) # check the height of the screen: 300 px
my_screen.exitonclick()

