from turtle import Turtle

class Text(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color('black')
    
  def set_text(self, state, x, y):
    # self.clear()
    self.goto(x, y)
    self.write(state, font=('sans-serif', 7, 'bold'))
