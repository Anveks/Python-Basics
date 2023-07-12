from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, coordinates):
    super().__init__()
    self.color('whitesmoke')
    self.shape('square')
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.position = coordinates
    self.goto(self.position)
    self.new_y = self.position[1]
  
  def up(self):
    if len(self.position) != 0:
      self.new_y += 10
      self.goto(self.position[0], self.new_y)
    
  def down(self):
    if len(self.position) != 0:
      self.new_y -= 10
      self.goto(self.position[0], self.new_y)