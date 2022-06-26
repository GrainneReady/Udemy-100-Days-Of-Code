# This program is to do with Udemy's Day 26 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022 (Instructor-led Course)
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365262/overview
#   https://replit.com/@appbrewery/day-26-2-exercise
# Instructions:
#   You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.
#   DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
# Example Output:
#   [2, 8, 34]
# Submission Result (100%)
#   https://i.gyazo.com/d49593f7664f44be6cdadba9f2d299a1.png

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

# Write your code 👆 above:

print(result)
