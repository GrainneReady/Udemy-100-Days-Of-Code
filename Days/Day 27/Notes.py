# +---------------------------+
# |        Section 27         |
# +---------------------------+
# | Tkinter, *args, **kwargs  |
# | and Creating GUI Programs |
# +---------------------------+

# Tkinter for Graphical User Interfaces
# Xerox created LAN, the first OOP language, the first GUI and computer mouse

# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# Creating windows and labels with Tkinter
from tkinter import *
# window = tkinter.Tk()   # Make a new window
# window.title(string="My First GUI Program")
# window.minsize(width=500, height=300)

# Create components to put inside the window
# Creating a Label:
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))  # NOTE: We will have to later specify how this label is to be laid out on the screen for it to show up
# You can leave out "normal" when making font as it is the default value, will only need to specify for things like bold, italic, etc. NOTE: bold, italic etc should be in lowercase
# my_label.pack(side="left")  # Will place label onto screen, will be centered by default but we can change the side to be left, bottom, top, ..., also
# my_label.pack(expand=True) # Will try to take up entire height and width of available screen size
# window.mainloop()   # NOTE: We need to call window.mainloop(), otherwise the window will not work, HAS to be at the end of the program

# Setting Default Values for Optional Arguments inside a Function Header

# Arguments with Default Values, can still be changed
# def my_function(a=1, b=2, c=3):
#     pass
#     pass
# Call my_function with b=5 instead of default value
# my_function(b=5)

# When hovering over function in python, if arg: str=... (notice the ...), then arg already has a default str value. likewise for other types
# args with default values are not required, but can be changed

# Example: This code will output '1, 4, 6'
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(1)

# NOTE: args is a Tuple
# *args: Many Positional Arguments
# Unlimited Arguments (Unlimited Positional Arguments)
# CHALLENGE: Modify the add function to take an unlimited number of arguments. ✔
#            Use a loop to sum all the arguments inside the function. ✔
#            Test it out by calling add() to calculate the sum of some arguments. ✔
# def add(*args):     # Can add as many arguments as we like, we NEED the asterisk (*) Can also be called something different like *numbers or *arguments
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 3, 5, 6, 5, 4, 3, 6, 7, 45)) # Position of arguments matters when using unlimited arguments

# NOTE: kwargs is a dict
# **kwargs: Many Keyworded Arguments
# def calculate(n, **kwargs):  # kwargs is a dictionary, (keyword = key, value = value)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

# class Car:
#
#     def __init__(self, **kw):
#         # kw - All optional args
#         self.make = kw.get("make")
#         # self.model = kw["model"]  # Will return an error if model was not given in args
#         self.model = kw.get("model")    # Will set model as None, preventing an error if model was not given in args
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")
#
#
# my_car = Car(make="Nissan", seats=4)
# print(my_car.model)

# Example: Will output '4 (7, 3, 0) {'x': 10, 'y': 64}
# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
# all_aboard(4, 7, 3, 0, x=10, y=64)

# Buttons, Entry, and Setting Component Options


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=new_text)


window = Tk()
window.title(string="My First GUI Program")
window.minsize(width=500, height=300)
# Add padding to all elements in window (add more space to edges of program), will also work for specific widgets in the widget.config()
window.config(padx=20, pady=20)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"  # Change text after object creation
my_label.config(text="New Text", padx=50, pady=50)    # Change text after object creation

# Button
# CHALLENGE: Show "Button Got Clicked" on my_label when the button gets clicked ✔
# CHALLENGE: When something is typed into Entry, change my_label to the text in Entry ✔

button = Button(text="Click Me", command=button_clicked)  # NOTE: Command only takes in function NAME, we DON'T include the ()
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
window.mainloop()

# Get value typed into Entry
input.get()

# https://i.gyazo.com/b4579041bf8ccc8869da285ba25da1aa.png Tkinter widgets

# Tkinter Layout Managers: pack(), place() and grid()
#   pack() places the widgets next to each other in a vaguely logical format, default side starting from the top, with every new widget below the previous widget
#       Issue: Difficult to specify exact position using pack()

#   place() is all about precise positioning, providing an x and y value
#       Issue: It's very precise, so we have to calculate and manage the coordinates that we want our widgets placed at by ourselves
#   my_label.place(x=0, y=0)

#   grid() is relative to other components, start from top left with col = 0 and row = 0 and go from there
#   my_label.grid(column=0, row=0)

# NOTE: Cannot mix up grid() and pack() in the same program

# CHALLENGE: Change up code that we have already written so that
#               Label is at col 0 row 0 ✔
#               New Button is at col 2 row 0 ✔
#               Button is at col 1 row 1 ✔
#               Entry is at col 3 row 2 ✔
