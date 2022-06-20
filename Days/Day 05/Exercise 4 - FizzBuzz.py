# This program is a direct copy of a program I made following Udemy's Day 5 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364939/overview
# Instructions:
#   You are going to write a program that automatically prints the solution to the FizzBuzz game.
#   Your program should print each number from 1 to 100 in turn.
#   When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#   When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#    And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# Example:
#   1
#   2
#   Fizz
#   4
#   Buzz
#   Fizz
#   7
#   8
#   Fizz
#   Buzz
#   11
#   Fizz
#   13
#   14
#   FizzBuzz # (continued...)
# Submission Result (100%):
#   https://i.gyazo.com/45f0a1ca7f70e6fa707bdfe7c2966205.png

#Write your code below this row 👇

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)