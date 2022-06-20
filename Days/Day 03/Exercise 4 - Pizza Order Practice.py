# This program is a direct copy of a program I made following Udemy's Day 3 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364925/overview
# Instructions:
#   Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#   Based on a user's order, work out their final bill.
#   Small Pizza: $15
#   Medium Pizza: $20
#   Large Pizza: $25
#   Pepperoni for Small Pizza: +$2
#   Pepperoni for Medium or Large Pizza: +$3
#   Extra cheese for any size pizza: + $1
# Example Input:
#   size = "L"
#   add_pepperoni = "Y"
#   extra_cheese = "N"
# Example Output:
#   Your final bill is: $28.
# Submission Result (100%):
#   https://i.gyazo.com/e117297a390a8a7ac5f8c501403370b0.png

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is: ${bill}.")

    