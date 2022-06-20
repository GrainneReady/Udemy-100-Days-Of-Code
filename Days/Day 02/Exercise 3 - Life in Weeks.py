# This program is a direct copy of a program I made following Udemy's Day 2 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364911/overview
# Instructions:
#   Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#   It will take your current age as the input, and output a message with our time left in this format:
#     You have x days, y weeks and z months left.
#     Where x, y, and z are replaced with the actual calculated numbers
# Example Input:
#   56
# Example Output:
#   You have 12410 days, 1768 weeks, and 408 months left.
# Submission Result (100%):
#   https://i.gyazo.com/f96ae6b9c312205a86b34cb113876937.png
# Personal Notes
#   This program from 100 Days of Code is not intended to take leap years into account.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

NUMBER_OF_DAYS_IN_A_YEAR = 365
NUMBER_OF_WEEKS_IN_A_YEAR = 52
NUMBER_OF_MONTHS_IN_A_YEAR = 12

ageAsInt = int(age)

yearsLeft = 90 - ageAsInt
daysLeft = yearsLeft * NUMBER_OF_DAYS_IN_A_YEAR
weeksLeft = yearsLeft * NUMBER_OF_WEEKS_IN_A_YEAR
monthsLeft = yearsLeft * NUMBER_OF_MONTHS_IN_A_YEAR
print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")