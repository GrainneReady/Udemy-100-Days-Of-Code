# This program is a direct copy of a program I made following Udemy's Day 8 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/364946/overview
# Instructions:
#   Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#   https://en.wikipedia.org/wiki/Prime_number
#   You need to write a function that checks whether if the number passed into it is a prime number or not.
#   e.g. 2 is a prime number because it's only divisible by 1 and 2.
#   But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Example Input 1:
#   73
# Example Output 1: 
#   It's a prime number
# Example Input 2:
#   75
# Example Output 2:
#   It's not a prime number
# Submission Result (100%):
#   https://i.gyazo.com/d1552aa5c254a49d8f7ce7d8f5c41342.png

#Write your code below this line 👇
import math
def prime_checker(number):
    isPrime = True
    i = 2
    for i in range(2, math.ceil(number/2)):
        if number % i == 0 and isPrime:
            print("It's not a prime number.")
            isPrime = False
    if (isPrime):
        print("It's a prime number.")
        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
