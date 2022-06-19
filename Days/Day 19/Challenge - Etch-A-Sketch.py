# This program is to do with Udemy's Day 19 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   None provided, instead compressed folders of the start and solution of the challenge were given.
# Instructions:
#   Create a turtle that will allow you to:
#     Press the 'w' key to go Forwards ✔
#     Press the 's' key to go Backwards ✔
#     Press the 'a' key to go Counter-Clockwise (left) ✔
#     Press the 'd' key to go Clockwise (right) ✔
#     Press the 'c' key to clear the drawing on screen ✔

from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clockwise():
    tim.left(10)


def turn_clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()
