from turtle import Screen
import time
from snake_model import Snake
from dot_model import Dot
from scoreboard_model import ScoreBoard

game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

dot = Dot()
scoreboard = ScoreBoard()
  
while game_on:
  screen.update()
  time.sleep(0.1) # adding a short delay
  snake.move()
  scoreboard.set_scoreboard()
  
  # collision with food:
  if snake.snake[0].distance(dot) < 15: # when a snake hits a dot - refresh random position
    dot.refresh()
    scoreboard.update_scoreboard()
    snake.extend()
  
  # collision with wall:
  if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
    game_on = False
    scoreboard.game_over()

  for segment in snake.snake[1:-1]:
    if snake.snake[0].distance(segment) < 10:
      game_on = False
      scoreboard.game_over()

screen.exitonclick()
