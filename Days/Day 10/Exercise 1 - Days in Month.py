# This program is a direct copy of a program I made following Udemy's Day 10 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365233/overview
# Instructions:
#   In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
#   it should return True if it is a leap year and return False if it is not a leap year.
#   You are then going to create a function called days_in_month() which will take a year and a month as inputs
#   The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
# Expected Input:
#   Enter a Year: 2022
#   Enter a Month: 2
# Expected Output:
#   28
# Submission Result (100%)
#   https://i.gyazo.com/ca2f92bc69fb049bf31464bd2526ec54.png

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, monthNumber):
    if monthNumber > 12 or monthNumber < 1:
        return ("Invalid Input: The month provided is not between 1 - 12.")
    elif year < 0:
        return("Invalid Input: The year provided cannot be a negative number.")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    monthIndex = monthNumber - 1
    if monthNumber == 2 and is_leap(year):
        return month_days[monthIndex] + 1
    else:
        return month_days[monthIndex]
  

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)