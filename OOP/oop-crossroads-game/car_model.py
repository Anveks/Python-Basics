from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()  
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())