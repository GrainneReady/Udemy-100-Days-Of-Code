# +------------+-----------------------------------------------+
# | Section 18 | Turtle Graphics, Tuples and Importing Modules |
# +------------+-----------------------------------------------+

# [keyword] [Module name] [keyword] [Thing in Module]
#   from        turtle      import      Turtle
# from turtle import Turtle, Screen
# import heroes   # If a module is not part of Python's standard library, you'll need to install it
# [keyword] [Module name] [keyword] [Everything]    # This can lead to confusion as somewhere down the line we may forget where methods come from
#   from        turtle      import      *

# Aliasing Modules
# [keyword] [Module name] [keyword] [alias name]
#   import      turtle      as          t
import turtle as t
import random

# Python Turtle: https://docs.python.org/3/library/turtle.html
#   Imagine it as a wandering turtle with a pen on its back and everywhere it goes, it leaves a line
#   tkinter is what the turtle module relies on to create these graphics
# Tkinter Colors: https://www.plus2net.com/python/tkinter-colors.php
# tim = Turtle()
# tim.shape("turtle")  # Changes timmy's shape to a turtle instead of an arrow, also works for things like circle, square, classic, arrow
# tim.color("DarkSeaGreen4")  # Change color to DarkSeaGreen4, aka #69698B or (105, 139, 105)
# tim.forward(100)  # Move forward by 100 paces
# tim.right(90)  # Turn right by 90°

# These next two lines have to be below any adjustments to our turtle
# screen = Screen()
# screen.exitonclick()

# print(heroes.gen())

# Python Tuples and How to Generate Random RGB Colours
#   Tuple (1, 3, 8)
#   List  [1, 3, 8]
# You cannot change the values of tuples like you can in lists
# Tuple does not support item assignment, or any sort of change of items
# Tuples are immutable
# Colors are often represented as Tuples
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

print(random_color())
