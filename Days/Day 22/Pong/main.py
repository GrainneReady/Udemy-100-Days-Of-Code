# I have originally made pong as part of CSU11013 Programming Project in Junior Freshman of Integrated Computer Science in Trinity College,
#   We used processing 3.0 and java to do it, this python version is far much more simpler, and was made to be in sync with the instructor's teachings.
# I plan to add my projects from CSU11013 to my github so that the more complex version of Pong along with some of my other projects can be seen
from turtle import Screen, right
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

left_paddle = Paddle(coordinates=(-350, 0))
right_paddle = Paddle(coordinates=(350, 0))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ball = Ball()
scoreboard = Scoreboard()

# 1. Create the Screen ✔
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("PyPong!")
screen.tracer(0)

screen.listen()
# Fixed bug where 'w' key could not be held down but the other move keys could 🔨
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)

game_is_on = True
while(game_is_on):
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    ball.wallCollisionCheck()
    ball.paddleCollisionCheck(paddle=left_paddle)
    ball.paddleCollisionCheck(paddle=right_paddle)
    ball.outOfBoundsCheck(scoreboard=scoreboard)

screen.exitonclick()
