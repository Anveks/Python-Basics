from turtle import Turtle, Screen

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.hideturtle()  # Hide the turtle initially
    self.penup()  # Lift the pen off the screen
    self.goto(0, 260)  # Set the position where the text will be displayed
    self.color("white")  # Set the text color
    
  def set_scoreboard(self):
    self.clear()
    self.write(f'Current score is: {self.score}', align="center", font=("Gothic", 16, "normal"))
    
  def update_scoreboard(self):
    self.score += 1
    self.set_scoreboard() 
    
  def game_over(self):
    self.goto(0, 150)
    self.write('Game Over.', align="center", font=("Gothic", 16, "normal"))