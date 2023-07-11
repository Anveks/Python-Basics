from turtle import Turtle, Screen
import random
import time

game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
squares = []
coordinates = [0,0]

for i in range(1, 4):
  square = Turtle()
  square.shape('square')
  square.penup()
  square.color('white')
  squares.append(square)
  square.goto(coordinates)
  coordinates[0] -= 20
  
while game_on:
  screen.update()
  time.sleep(0.1) # adding a short delay
  
  for square in range(len(squares) - 1, 0, -1):
    x = squares[square - 1].xcor()
    y = squares[square - 1].ycor()
    squares[square].goto(x, y)
    
  squares[0].forward(20)
  squares[0].left(90)  
    
    



screen.exitonclick()
