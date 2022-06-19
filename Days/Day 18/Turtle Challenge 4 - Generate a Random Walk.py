# This program is to do with Udemy's Day 18 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://replit.com/@appbrewery/day-18-4-start
#   https://replit.com/@appbrewery/day-18-4-final (Solution)
# Instructions:
#   Make your turtle do a random walk (A path that consists of a succession of random steps on some mathematical space) ✔
#   Each time it progresses by the same distance, but randomly chooses a direction to go along with a random color ✔
#   See if you can increase the line thickness ✔
#   See if you can figure out how to increase the speed of the turtle so it draws much faster ✔

import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]
tim.pensize(width=15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(20)

screen = t.Screen()
screen.exitonclick()
