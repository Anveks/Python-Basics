import time
from turtle import Screen
from player_model import Player
from car_model import Car
from scoreboard_model import ScoreBoard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, 'Up')

cars = []  # List to store the car instances

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate a car randomly
    if random.randint(0, 15) < 5:
        new_car = Car()
        cars.append(new_car)

    # Move each car
    for car in cars:
        car.move()
        if player.ycor() > 280:
            player.reset()
            car.increase_speed()
            scoreboard.update_scoreboard()

    # Check for collisions with the player
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
