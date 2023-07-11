from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
  tim.fd(10)
  
def move_backwards():
  tim.backward(10)

def move_left():
  tim.left(45)
  
def move_right():
  tim.right(45)
  
def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()
  
screen.listen()
screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_backwards, 's')
screen.onkeypress(move_left, 'a')
screen.onkeypress(move_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()