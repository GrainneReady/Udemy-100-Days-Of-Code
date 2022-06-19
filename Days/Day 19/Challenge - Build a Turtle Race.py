# This program is to do with Udemy's Day 19 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   None provided, instead compressed folders of the start and solution of the challenge were given.
# Instructions:
#   Build a Turtle Race ✔
#   Make a popup at the beginning which will ask the user to make a bet on which colour they think will win. "Who will win the race? Enter a colour:" ✔
#   The turtle colours will be the colours of the rainbow ✔
#   Once a bet on a colour is made, the turtles will line up in the starting position on the far left of the screen ✔
#   The turtles will all start making random steps towards the right edge of the screen ✔
#   The first turtle to reach past the right edge of the screen will be the winner ✔
#   When the winner has been determined, the screen will exit and it will print out if your bet was correct or not ✔
#   If the bet was correct, it will print "You've won! The {winner_colour} turtle is the winner!" ✔
#   If the bet was incorrect, it will print "You've lost! The {winner_colour} turtle is the winner!" ✔
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for turtle_index in range(len(colors)):
    currentTurtle = Turtle(shape="turtle")
    currentTurtle.penup()
    currentTurtle.color(colors[turtle_index])
    currentTurtle.goto(x=-230, y=-100 + (turtle_index * 30))
    turtles.append(currentTurtle)
if user_bet in colors:
    race_underway = True
while race_underway:
    for turtle in turtles:
        steps_forward = random.randint(0, 10)
        turtle.forward(steps_forward)
        if turtle.xcor() >= 230:
            winner_colour = turtle.pencolor()
            race_underway = False

if user_bet == winner_colour:
    print(f"You've won! The {winner_colour} turtle is the winner!")
else:
    print(f"You've lost! The {winner_colour} turtle is the winner!")
