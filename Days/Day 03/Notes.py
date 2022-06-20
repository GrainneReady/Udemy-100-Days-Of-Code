# Section 3: Day 3 - Control Flow and Logical Operators

# if statements need proper indentation. There will be an indentation error if the indentation is not correct.
# if statement template
# if condition:
#   do x
# else:
#   do y

# draw.io is useful for drawing diagrams
# This is an example diagram provided by 100 Days of Code about how you need to be above a certain height to be eligible to go on a ride in a theme park
# If the person's height is greater than 120cm, they can ride the rollercoaster.
# https://i.gyazo.com/d4299f5f3a2536b00397d560cd5708aa.png

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height > 120:
#    print("Congratulations, you can ride the rollercoaster!")
#else:
#    print("Sorry, you are not tall enough to ride the rollercoaster.")
    
# Comparison Operators
#   >   |   Greater Than
#   <   |   Less Than
#   >=  |   Greater Than or Equal To
#   <=  |   Less Than or Equal To
#   ==  |   Equal To
#   !=  |   Not Equal to

# One equal sign (=) is an Assignment, whereas two equal signs (==) checks for Equality.

# This is an example diagram provided by 100 Days of Code about how you need to be above a certain height to be eligible to go on a ride in a theme park
# This is a more advanced version of the previous example
# https://i.gyazo.com/99d242e4fa26994b961c38ef7d1a3dde.png

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 45 and age < 55:
        bill = 0
        print("Everything is goign to be ok. Have a free ride on us!")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12.")
    elif age >= 12:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 5
        print("Child tickets are $5.")
    photosRequested = bool(input("Do you want photos for an extra $3 (Yes/No)? "))
    if photosRequested:
        bill += 3
    print(f"Your total bill is {bill}")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")
    
# Logical Operators
# A and B, when both conditions are true, returns true, else is false
# C or D, when either or or both the conditions are true, returns true. Else is false
# not E, if E is true, return false, otherwise return true