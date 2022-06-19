# This program is to do with Udemy's Day 18 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://replit.com/@appbrewery/day-18-3-start
#   https://replit.com/@appbrewery/day-18-3-final (Solution)
# Instructions:
#   Draw Shapes ✔
#   Each shape has a different color chosen at random ✔

import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
DEGREES_IN_A_CIRCLE = 360
SIDES_IN_A_TRIANGLE = 3
SIDES_IN_A_DECAGON = 10


def color_changer(turtle):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r, g, b)


def draw_shape(sides, turtle):
    color_changer(turtle)
    angle = DEGREES_IN_A_CIRCLE / sides
    for _ in range(sides):
        tim.forward(100)
        tim.setheading(tim.heading() + angle)


for sides in range(SIDES_IN_A_TRIANGLE, SIDES_IN_A_DECAGON + 1):
    draw_shape(sides=sides, turtle=tim)

screen = t.Screen()
screen.exitonclick()
