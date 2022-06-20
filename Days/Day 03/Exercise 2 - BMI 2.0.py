# This program is a direct copy of a program I made following Udemy's Day 3 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364916/overview
# Instructions:
#   Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
#   It should tell them the interpretation of their BMI based on the BMI value.
#   * Under 18.5 if they are underweight
#   * Over 18.5 but below 25 they have a normal weight
#   * Over 25 but below 30 they are slightly overweight
#   * Over 30 but below 35 they are obese
#   * Above 35 they are clinically obese.
# Example Input:
#   weight = 85
#   height = 1.75
# Example Output:
#   Your BMI is 28, you are slightly overweight.
# Submission Result (100%):
#   https://i.gyazo.com/844b7df5b5ca37f4b0680b91ec66e5e5.png

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


BMI = round(weight / height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
    