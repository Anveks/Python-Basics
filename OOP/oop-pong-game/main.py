from turtle import Screen
from paddle_model import Paddle
from ball_model import Ball
from scoreboard_model import ScoreBoard

game_on = True
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0) # disable all the animations

paddle_a = Paddle((350, 0))
paddle_b = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(paddle_a.up, 'Up')
screen.onkeypress(paddle_a.down, 'Down')
screen.onkeypress(paddle_b.up, 'w')
screen.onkeypress(paddle_b.down, 's')

while game_on:
  screen.update()
  ball.move()
  
  if ball.ycor() > 290 or ball.ycor() < -290:
    ball.bounce_y()
    
  if ball.distance(paddle_a) < 50 and ball.xcor() > 320 or ball.distance(paddle_b) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    
  if ball.xcor() > 380:
    scoreboard.l_point()  # Update the score for player A
    scoreboard.update_scoreboard()  # Update the scoreboard
    
    ball.reset()
    
  if ball.xcor() < -380:
    scoreboard.r_point()  # Update the score for player B
    scoreboard.update_scoreboard()  # Update the scoreboard
    
    ball.reset()

screen.exitonclick()
