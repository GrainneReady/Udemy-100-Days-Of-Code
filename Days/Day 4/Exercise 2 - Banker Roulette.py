# This program is a direct copy of a program I made following Udemy's Day 4 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364928/overview
# Instructions:
#   You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#   Important: You are not allowed to use the choice() function.
#   Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed
#     by comma then space. e.g. name, name, name
#   When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.
# Example Input:
#   Angela, Ben, Jenny, Michael, Chloe
# Example Output:
#   Michael is going to buy the meal today!
# Submission Result (100%):
#   https://i.gyazo.com/59d5ee844e7d2db1256c177590a512af.png

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

person_who_will_pay = names[random.randint(0, len(names) - 1)]

print(f"{person_who_will_pay} is going to buy the meal today!")
