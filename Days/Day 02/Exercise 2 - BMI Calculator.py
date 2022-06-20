# This program is a direct copy of a program I made following Udemy's Day 2 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364910/overview
# Instructions:
#   Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#   The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and
#     a short person both weigh the same amount, the short person is usually more overweight.
#   The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Example Input:
#   weight = 80
#   height = 1.75
# Example Output:
#   26
# Submission Result (100%):
#   https://i.gyazo.com/4d535df093d5bcca69ac56e91c4f903d.png
# Personal Notes:
#   All information inputted using input() will automatically be set to dataType string
#   This exercise from 100 Days of Code is purposefully not taking rounding into account
#     in future, we should use the round(numberToRound, numberOfDecimalPlacesToRoundTo) function.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightSquared = float(height) ** 2
BMI = int(float(weight) / heightSquared)
print(str(BMI))