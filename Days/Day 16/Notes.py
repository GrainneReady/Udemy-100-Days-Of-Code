# Section 16 - OOP!
# Object Oriented Programming

# We were doing procedural programming, one of the earliest paradigms of programming.
# The increase in number relationships that we need to remember and manage gets very confusing

# How would we implement it?
# Example:
#   4 Types of staff in a restaurant, chef, waiter, cleaner and then a manager who manages them all
#   To model a waiter, we need what it has and what it does, is_holding_plate, tables_responsible_for, takes_order(), takes_payment()...
#   Two main things, attributes and its methods. attributes are is_holding_plate or tables_responsible_for. Methods are takes_order() and takes_payment()
#   We call it a method as its a function that a waiter object can do
# We are trying to model real life objects.
# They have attributes (usually modelled with variables)
# The things they can do are called methods (usually modelled by functions)
# An object is basically just a way of combining a piece of data (attributes) with some functionality (methods) altogether in the same thing
# We can have multiple objects generated as the same type. Multiple waiters, making 'Waiter' a class, and the different waiters an 'Object'. It's called blueprinting

# Constructing Objects
# A car would have attributes like fuel_left, mileage combined with the functionality like the ability to drive, stop, break
# The blueprint which models this is called a class, from this class we can generate as many objects as we want
# The object is the actual thing we're going to be using in our code
# car = CarBlueprint()
# NOTE: Classes are usually written in Pascal case (PascalCase, CarBlueprint) where first letter is capitalised and there are no spaces or '_'
#       This is to differentiate it from all the variable and function names we gave in Python, where each word is separated by underscores '_'
# All we need is to declare our object (In previous example it was car), set it to the class, and include the parenthesis, which will construct the object from the blueprint

# Turtle Graphics
# https://docs.python.org/3/library/turtle.html
# Colors: https://cs111.wellesley.edu/reference/colors
# import another_module
# import turtle               # Fetch class Turtle from turtle module, and use () to construct the object, and then the name 'timmy' to save the object
# from turtle import Turtle, Screen   # We can also use this, which will now allow us to construct a new object timmy2

# timmy = turtle.Turtle()
# timmy = Turtle()
# print(timmy)        # Printing these will show that there is a turtle.Turtle object at a specific address in memory
# timmy.shape("turtle")  # Changes timmy into shape of a turtle, instead of an arrow
# timmy.color("OliveDrab")
# Challenge: Get the turtle to move forward by 100 paces
# turtle.forward(100)


# Object attributes: from object get attribute
# car.speed (Object = car, Attribute = speed)

# my_screen = Screen()
# print(my_screen.canvheight)  # Height is preset to 300
# my_screen.exitonclick()  # Allows screen to continue running until we click on the screen. Our code will only exit once we click


# Object Methods for class Car
# Only difference in using these functions in comparison to other functions we've used in procedural programming is the syntax
#   car.stop()
# Methods:
# def move():
#   speed = 60
#
# def stop():
#   speed = 0

# Python Packages
# pypi.org
# To import a package, stop debugging and use the Command Pallete to run Terminal: Create New Terminal (Ctrl + Shift + ')
# This will open a command prompt for selected interpreter
# A best practice among Python developers is to avoid installing packages into a global interpreter environment.
# You instead use a project-specific virtual environment that contains a copy of a global interpreter.
# Once you activate that environment, any packages you then install are isolated from other environments.
# Such isolation reduces many complications that can arise from conflicting package versions.
# To create a virtual environment and install packages, enter the following commands:
# 1. Create and Activate the virtual environment
#    NOTE: when you create a new virtual environment, you should be prompted by VS Code to set it as the default for your workspace folder.
#    py -3 -m venv .venv
#    .venv\scripts\activate
#    If that generated the Message "Activate.ps1 is not digitally signed...", you need to enter the following which changes execution policy to allow scripts to run
#    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# 2. Select your new environment by using the Python: Select Interpreter command from the Command Palette
# 3. Install the packages
#    python -m pip install prettytable
# Once done, type deactivate in the terminal window to deactivate the virtual environment
from prettytable import PrettyTable
# Challenge: Create a PrettyTable object and save it to a variable called table
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
