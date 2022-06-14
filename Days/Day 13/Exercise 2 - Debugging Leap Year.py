# This program is to do with Udemy's Day 13 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365235/overview
# Instructions:
#   Read this the code in main.py
#   Spot the problems 🐞.
#   Modify the code to fix the program.
#   No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# Submission Result (100%)
#   https://i.gyazo.com/d24edd6fb6bb1962b9371d306d4f22cf.png

year = int(input("Which year do you want to check?"))    # Original Line: year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")