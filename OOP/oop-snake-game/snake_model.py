from turtle import Turtle

START_COORDINATES = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.snake = []
    self.create_snake()
  
  def create_snake(self):
    for coordinates in START_COORDINATES:
      self.add_segment(coordinates)
      
  def move(self):    
      for segment in range(len(self.snake) - 1, 0, -1):
        x = self.snake[segment - 1].xcor()
        y = self.snake[segment - 1].ycor()
        self.snake[segment].goto(x, y)
      self.snake[0].forward(MOVE_DISTANCE)
      
  def add_segment(self, coordinates):
      snake_segment = Turtle('square')
      snake_segment.shape('square')
      snake_segment.penup()
      snake_segment.color('white')
      snake_segment.goto(coordinates)
      self.snake.append(snake_segment)
    
  def extend(self):
    self.add_segment(self.snake[-1].position())
      
  def up(self):
    if self.snake[0].heading() != DOWN: self.snake[0].setheading(UP)
    
  def down(self):
    if self.snake[0].heading() != UP: self.snake[0].setheading(DOWN)
    
  def left(self):
    if self.snake[0].heading() != RIGHT: self.snake[0].setheading(LEFT)
    
  def right(self):
    if self.snake[0].heading() != LEFT: self.snake[0].setheading(RIGHT)