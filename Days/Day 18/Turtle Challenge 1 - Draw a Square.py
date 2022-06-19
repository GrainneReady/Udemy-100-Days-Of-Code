# This program is to do with Udemy's Day 18 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://replit.com/@appbrewery/day-18-1-start
#   https://replit.com/@appbrewery/day-18-1-final (Solution)
# Instructions:
#   Draw a Square ✔

#####Turtle Intro######
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
# tim.forward(100)
# tim.backward(200)
# tim.right(90)
# tim.left(180)
# tim.setheading(0)


######## Challenge 1 - Draw a Square ############
for i in range(4):
    tim.forward(100)
    tim.left(90)
