from turtle import Turtle

START_COORDINATES = [(0, 0), (20, 0), (40, 0)]

class Snake:
  def __init__(self):
    self.squares = []
    self.create_snake()
  
  def create_snake(self):
    for coordinates in START_COORDINATES:
      snake_segment = Turtle('square')
  