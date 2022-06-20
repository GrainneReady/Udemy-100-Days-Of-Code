from turtle import Screen, Turtle
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)

snake = Snake()

screen.listen()
# Challenge: Create up, down, left, and right methods in snake to move the snake in the respective direction
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Challenge: Create 3 separate squares(20x20), which are each turtle objects that are white in color. The first is positioned at (0, 0)
#               the next is 20 pixels to the left and the next is 20 pixels to the left after that. ✔
# Challenge: Extract existing snake code into a snake class ✔

game_is_on = True
while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()    # This has to be the last line for screen stuff
