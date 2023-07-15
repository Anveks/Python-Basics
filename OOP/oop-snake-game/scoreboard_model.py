from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.filename = 'OOP/oop-snake-game/data.txt'
        self.highscore = self.get_score()  # Set the default highscore

    def set_scoreboard(self):
        self.clear()
        self.write(f'Current score is: {self.score} | Highscore: {self.highscore}', align="center", font=("Gothic", 16, "normal"))

    def update_scoreboard(self):
        self.score += 1
        self.set_scoreboard()
        
    def get_score(self):
        with open(self.filename, mode='r') as file:
          saved_score = file.read()
          if saved_score != 0: return int(saved_score)

    def save_score(self):
        with open(self.filename, mode='w') as file:
            file.write(str(self.highscore))
            print('File rewritten.')

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_score()
        self.score = 0
        self.set_scoreboard()
