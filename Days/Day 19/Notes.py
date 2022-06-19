# +----------------------------------------------+
# |                  Section 19                  |
# +----------------------------------------------+
# | Instances, States and Higher Order Functions |
# +----------------------------------------------+

# Turtle Event Listeners
from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="space", fun=move_forwards)    # Function as Inputs, better to use keyword arguments than positional arguments in these cases. onkey() is a higher order function
screen.exitonclick()

# Functions as Inputs
# 
# 
# def function_a(something):
#     # Do this with something
#     # Then do this
#     # Finally do this
#     pass
# 
# 
# def function_b():
#     # Do this
#     pass
# 
# 
# function_a(function_b)

# Higher Order Functions
# Higher order functions are functions that can work with other functions, previously, function_a was a higher order function

# Object State and Instances
timmy = Turtle()        # Instance (Turtle object)
timmy.color("green")    # State of Timmy's color attribute is "green"
tommy = Turtle()        # Instance (Turtle object)
tommy.color("purple")   # State of Tommy's color attribute is "purple"
# timmy and tommy are instances of Turtle object and as such their attributes are instance attributes, variables belonging to only them (as an object)
# An instance of a class is an object
# Timmy and Tommy act completely independently of each other
# The method calls for timmy and tommy are not matched. Tommy could be in the process of moving while Timmy is completely stationary
