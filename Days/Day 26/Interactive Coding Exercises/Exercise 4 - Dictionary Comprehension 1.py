# This program is to do with Udemy's Day 26 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022 (Instructor-led Course)
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365274/overview
#   https://replit.com/@appbrewery/day-26-4-exercise
# Instructions:
#   You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
#   Try Googling to find out how to convert a sentence into a list of words.
#   Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Example Output:
#   {
#   'What': 4,
#   'is': 2,
#   'the': 3,
#   'Airspeed': 8,
#   'Velocity': 8,
#   'of': 2,
#   'an': 2,
#   'Unladen': 7,
#   'Swallow?': 8
#   }
# Submission Result (100%)
#   https://i.gyazo.com/c573ef2b0fdbc84cddd9020c19d3c3dc.png

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word: len(word) for word in sentence.split()}

print(result)
