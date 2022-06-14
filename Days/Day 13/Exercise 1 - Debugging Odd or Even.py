# This program is to do with Udemy's Day 13 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365234/overview
#   https://replit.com/@appbrewery/day-13-1-exercise#main.py
# Instructions:
#   Read this the code in main.py
#   Spot the problems 🐞.
#   Modify the code to fix the program.
#   Fix the code so that it works and passes the tests when you submit.
# Submission Result (100%)
#   https://i.gyazo.com/68f2d78394d8f7228c0e9b044dcdd048.png

number = int(input("Which number do you want to check?"))

if number % 2 == 0:     # Original Line: if number % 2 = 0: (fixed)
  print("This is an even number.")
else:
  print("This is an odd number.")
  