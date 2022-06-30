# This program is to do with Udemy's Day 30 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022 (Instructor-led Course)
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365278/overview
#   https://replit.com/@appbrewery/day-30-1-exercise
# Instructions:
#   We've got some buggy code. Try running the code. The code will crash and give you an IndexError.
#   This is because we're looking through the list of fruits for an index that is out of range.
#   Use what you've learnt about exception handling to prevent the program from crashing.
#   If the user enters something that is out of range just print a default output of "Fruit pie". e.g.
# Submission Result (100%)
#   https://i.gyazo.com/3613b61cc93f70f084fc20b3a63932ac.png

fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing. ✔


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
