from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('black')
    self.penup()
    self.hideturtle()
    self.level = 1
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-280, 260)  # Adjusted coordinates
    self.write('Level: ' + str(self.level), align='left', font=FONT)
    self.level += 1

  def game_over(self):
    self.goto(0, 150)
    self.write('Game Over.', align="center", font=("Gothic", 16, "normal"))