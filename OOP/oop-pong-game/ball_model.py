from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('pink')
    self.penup()
    self.goto(0, 0)
    self.x_move = 0.05
    self.y_move = 0.05
    
  def move(self):
    new_x = self.xcor() + self.x_move  # Increment the x-coordinate by 1
    new_y = self.ycor() + self.y_move  # Increment the y-coordinate by 1
    self.goto(new_x, new_y)
  
  def bounce_y(self):
    self.y_move *= -1 # changing the y_move to its negative value thus reversing the direction
    
  def bounce_x(self):
    self.x_move *= -1
    
  def increase_speed(self):
    self.x_move *= 0.05
    self.y_move *= 0.05
    
  def reset(self):
    self.x_move = 0.05
    self.y_move = 0.05
    # self.position(0, 0)
    self.bounce_x()