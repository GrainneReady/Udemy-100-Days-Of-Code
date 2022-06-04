# This program is a direct copy of a program I made following Udemy's Day 2 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364906/overview
# Instructions:
#   Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Example Input:
#   39
# Example Output:
#   12
# Submission Result (100%):
#   https://i.gyazo.com/275e99b6f86b841197b4bd824bb658a4.png
# Personal Notes:
#   To change a data type of a variable, you can use dataType(variable)
#    for example, if a = 5, this will give us an int. If we want it to be a string, we instead use a = str(5).

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇

# Extract each of the two digits from the inputted number and change to int DataType
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# We can set the sum as a variable instead of printing it out straight away
sum_of_digits = first_digit + second_digit

# Print out the Sum of the Digits
print(sum_of_digits)
