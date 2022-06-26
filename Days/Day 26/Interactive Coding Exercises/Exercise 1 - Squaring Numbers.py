# This program is to do with Udemy's Day 26 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022 (Instructor-led Course)
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365244/overview
#   https://replit.com/@appbrewery/day-26-1-exercise
# Instructions:
#   You are going to write a List Comprehension to create a new list called squared_numbers.
#   This new list should contain every number in the list numbers but each number should be squared.
#   e.g.
#     4 * 4 = 16
#     4 squared equals 16.
# Example Output:
#   [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
# Submission Result (100%)
#   https://i.gyazo.com/f2e08048a613749a236c588744a82325.png


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num**2 for num in numbers]

# Write your code 👆 above:

print(squared_numbers)
