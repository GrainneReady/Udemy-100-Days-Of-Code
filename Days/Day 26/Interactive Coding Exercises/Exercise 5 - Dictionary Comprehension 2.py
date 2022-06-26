# This program is to do with Udemy's Day 26 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022 (Instructor-led Course)
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   (The course made a mistake and forgot to add this exercise to codingroom, so we just have the replit links)
#   https://replit.com/@appbrewery/day-26-5-exercise
#   https://repl.it/@appbrewery/day-26-5-test-your-code
# Instructions:
#   You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
#   To convert temp_c into temp_f:
#   (temp_c * 9/5) + 32 = temp_f
#   Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Example Output:
#   {
#   'Monday': 53.6,
#   'Tuesday': 57.2,
#   'Wednesday': 59.0,
#   'Thursday': 57.2,
#   'Friday': 69.8,
#   'Saturday': 71.6,
#   'Sunday': 75.2
#   }
# Submission Result(✔): (Forced to use replit tests instead of codingroom, passes all test cases)
#   https://i.gyazo.com/28efdec3047575fec42d77218cb0c73a.png

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
