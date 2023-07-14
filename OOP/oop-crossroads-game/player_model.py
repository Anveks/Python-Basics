from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)  # Set the turtle's heading to face upwards
        
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE  # Calculate the new y-coordinate
        self.goto(self.xcor(), new_y)  # Move to the new position on the y-axis
        
    
