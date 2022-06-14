# This program is to do with Udemy's Day 13 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365243/overview
# Instructions:
#   Read this the code in main.py
#   Spot the problems 🐞.
#   Modify the code to fix the program.
#   No shortcuts - don't copy-paste to replace the code entirely with a working solution.
#   The code needs to print the solution to the FizzBuzz game.
#   Your program should print each number from 1 to 100 in turn.
#   When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#   When the number is divisible by 5, then instead of printing the number it should print "Buzz".
#     And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# Submission Result (100%)
#   https://i.gyazo.com/d24edd6fb6bb1962b9371d306d4f22cf.png

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # Original Line: if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0: # Original Line: if number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0: # Original Line: if number % 5 == 0:
    print("Buzz")
  else:
    print(number)   # Original Line: print([number])
