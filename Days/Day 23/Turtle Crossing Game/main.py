# Difficulty Chosen - "Difficulty Expert 🤯: Only use Step 1 to complete the project." ✔
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if player.finishLineCheck():            # Check to see if player has reached finish line (top of screen)
        car_manager.increment_cars_speed()
        scoreboard.update_level()

    if car_manager.collisionCheck(player):  # Check to see if player has collided with any of the cars, if so, game over
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
