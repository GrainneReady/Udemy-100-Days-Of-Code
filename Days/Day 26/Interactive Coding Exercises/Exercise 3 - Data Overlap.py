# This program is to do with Udemy's Day 26 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022 (Instructor-led Course)
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365263/overview
#   https://replit.com/@appbrewery/day-26-3-exercise
# Instructions:
#   💪 This exercise is HARD
#   Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#   You are going to create a list called result which contains the numbers that are common in both files.
#   e.g. if file1.txt contained:
#     1
#     2
#     3
#   and file2.txt contained:
#     2
#     3
#     4
#   result = [2, 3]
#   IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
# Example Output:
#   [3, 6, 5, 33, 12, 7, 42, 13]
# Submission Result (100%)
#   https://i.gyazo.com/eaeb5689801c7c75518f0bab35294053.png

with open("Days\\Day 26\\Interactive Coding Exercises\\file1.txt") as file_1:
    file_1_numbers = file_1.readlines()
with open("Days\\Day 26\\Interactive Coding Exercises\\file2.txt") as file_2:
    file_2_numbers = file_2.readlines()

result = [int(num) for num in file_1_numbers if num in file_2_numbers]

# Write your code above 👆

print(result)
