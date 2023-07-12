from turtle import Screen
from paddle_model import Paddle
from ball_model import Ball

game_on = True
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0) # disable all the animations

paddle_a = Paddle((350, 0))
paddle_b = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle_a.up, 'Up')
screen.onkeypress(paddle_a.down, 'Down') # when we use a func as a parameter of another func we do not need to call it; otherwise we will get a fucntion's value instead
screen.onkeypress(paddle_b.up, 'w')
screen.onkeypress(paddle_b.down, 's')

while game_on:
  if ball.ycor() > 290 or ball.ycor() < -290:
    ball.bounce()
  screen.update()
  ball.move()







screen.exitonclick()