# This program is made following Udemy's Day 2 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#      https://www.udemy.com/course/100-days-of-code/
# Preview URLs:
#      https://replit.com/@appbrewery/tip-calculator-start#README.md
#      https://replit.com/@appbrewery/tip-calculator-end#main.py
# Instructions:
#   If the bill was $150.00, split between 5 people, with 12% tip.
#   Each person should pay (150.00 / 5) * 1.12 = 33.6
#   Format the result to 2 decimal places = 33.60
#   Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
#   Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Example Input:
#   Welcome to the tip calculator!
#   What was the total bill? $124.56
#   How much tip would you like to give? 10, 12, or 15? 12
#   How many people to split the bill? 7
# Example Output:
#   Each person should pay: $19.93
# Personal Notes:
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
numberOfPeople = int(input("How many people to split the bill? "))

tipAsPercentage = tip/100
totalTip = bill * tipAsPercentage
billWithTip = bill + totalTip

amountToBePaidEach = round(billWithTip / numberOfPeople, 2)
# amountToBePaidEach = "{:.2f}.format(billWithTip / numberOfPeople"

print(f"Each person should pay: ${amountToBePaidEach}")


