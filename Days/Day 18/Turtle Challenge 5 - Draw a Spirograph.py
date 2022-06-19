# This program is to do with Udemy's Day 18 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://replit.com/@appbrewery/day-18-5-start
#   https://replit.com/@appbrewery/day-18-5-final (Solution)
# Instructions:
#   Make a Spirograph ✔
#   Make the turtle draw a number of circles, each with a radius of 100 ✔
#   Each circle should have a random color, and have a different tilt ✔

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########
tim.speed("fastest")


def draw_spirograph(size_of_tilt):
    for _ in range(int(360 / size_of_tilt)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_tilt)
        tim.circle(100)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
