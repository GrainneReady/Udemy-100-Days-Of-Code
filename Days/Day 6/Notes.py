# Section 6 - Functions, Code Blocks and While Loops

# Functions:
# print() is a function, like len(), sum(), int(), etc.
num_char = len("Hello")
print(num_char)

# Defining a function
def my_function():
    print("Hello")
    print("Bye")

# Calling a function
my_function()

# The next part of the lectures are done in reeborg
#   https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json


# Indentation:
def my_second_function():
    print("Inside Function 1")

# If we wanted to add more code to my_second_function, we would need to indent it like so:
#def my_second_function():
#    print("Inside Function 1")
#    print("Inside Function 2")

# If we wanted to add more code but have it outside the function, we would need to do this:
#def my_second_function():
#    print("Inside Function")
#print("Outside Function")
sky = "clear"
def my_third_function():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("Hello")
print("World")

my_third_function()

# While Loop:
# while something_is_true:
#   print("Doing something")