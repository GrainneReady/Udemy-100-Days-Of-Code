# This program is a direct copy of a program I made following Udemy's Day 1 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364789/overview
# Instructions:
#   Write a program that switches the values stored in the variables a and b.
# Example Input:
#   a: 3
#   b: 5
# Example Output:
#   a: 5
#   b: 3
# Submission Result (100%):
#   https://i.gyazo.com/98a01c2fa8763c0e35dd90b43b842aa5.png

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a;
a = b;
b = c;
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)