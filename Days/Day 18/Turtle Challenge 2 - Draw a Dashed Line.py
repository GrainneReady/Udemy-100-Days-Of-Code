# This program is to do with Udemy's Day 18 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://replit.com/@appbrewery/day-18-2-start
#   https://replit.com/@appbrewery/day-18-2-final (Solution)
# Instructions:
#   Draw a Dashed Line ✔
import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for i in range(40):
    if tim.isdown():    # isdown() returns True if pen is down and False if pen is up
        tim.penup()     # Puts pen up (stops drawing when moving)
    else:
        tim.pendown()   # Puts pen down (starts drawing when moving)
    tim.forward(10)     # Moves forward by 10 paces

screen = t.Screen()
screen.exitonclick()
