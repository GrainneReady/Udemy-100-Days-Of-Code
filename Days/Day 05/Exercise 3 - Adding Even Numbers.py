# This program is a direct copy of a program I made following Udemy's Day 5 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364936/overview
# Instructions:
#   You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
#   i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#   Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
#   You are required to use the range() function
# Submission Result (100%):
#   https://i.gyazo.com/7837957e98183ee216465aed6b3eb663.png

#Write your code below this row 👇

sumOfEvenNumbers = 0
for number in range(2, 101, 2):
    sumOfEvenNumbers += number
print(sumOfEvenNumbers)
