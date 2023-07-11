from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle would win the race? Color: ')
colors = ['blue', 'red', 'purple', 'orange']
all_turtles = []

coordinates = [-240, -90]  # Update the initial x-coordinate to position turtles on the left

for color in colors:
    t = Turtle(shape='turtle')
    t.color(color)
    t.penup()
    t.goto(coordinates)
    coordinates[1] += 50  # Move turtles upward for spacing
    all_turtles.append(t)
    
if user_bet:
  race_on = True
  
while race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      race_on = False
      winner = turtle.pencolor()
      if winner == user_bet: print('You won!')
      else: print('Good luck nex time!')
    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)
  
screen.exitonclick()
