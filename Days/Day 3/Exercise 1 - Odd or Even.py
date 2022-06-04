# This program is a direct copy of a program I made following Udemy's Day 3 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364915/overview
# Instructions:
#   Write a program that works out whether if a given number is an odd or even number
#   Even numbers can be divided by 2 with no remainder
#   e.g. 86 is even because 86 / 2 = 43
#   43 does not have any decimal places, Therefore the division is clean
#   e.g. 59 is odd because 59 / 2 = 29.5
#   29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
#   The modulo is written as a percentage sign(%) in Python. It gives you the remainder after a division
#   e.g.
#   6 % 2 = 3 with no remainder
#     Therefore 6 % 2 = 0
#   5 / 2 = 2 x 2 + 1, the remainder is 1
#     Therefore: 5 / 2 = 1
#   14 / 4 = 3 x 4 + 2, remainder is 2
#     Therefore: 14 % 4 = 2
# Example Input:
#   43
# Example Output:
#   This is an odd number
# Submission Result (100%):
#   https://i.gyazo.com/512e2a4ffa6cd8c7e55e7a1e2e0e5b26.png

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")