# This program is a direct copy of a program I made following Udemy's Day 3 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364926/overview
# Instructions:
#   You are going to write a program that tests the compatibility between two people.
#   To work out the love score between two people:
#   Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#   Then check for the number of times the letters in the word LOVE occurs. 
#   Then combine these numbers to make a 2 digit number.
#   For Love Scores less than 10 or greater than 90, the message should be:
#   "Your score is **x**, you go together like coke and mentos."
#   For Love Scores between 40 and 50, the message should be:
#   "Your score is **y**, you are alright together."
#   Otherwise, the message will just be their score. e.g.:
#   "Your score is **z**."
#   e.g.
#   name1 = "Angela Yu"
#   name2 = "Jack Bauer"
#   T occurs 0 times
#   R occurs 1 time
#   U occurs 2 times
#   E occurs 2 times
#   Total = 5
#   L occurs 1 time
#   O occurs 0 times
#   V occurs 0 times
#   E occurs 2 times
#   Total = 3
#   Love Score = 53
#   Print: "Your score is 53."
# Example Input:
#   name1 = "Kanye West"
#   name2 = "Kim Kardashian"
# Example Output:
#   Your score is 42, you are alright together.
# Submission Result (100%):
#   https://i.gyazo.com/90817280bd4201bd319947ec42f81257.png

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1UpperCase = name1.upper()
name2UpperCase = name2.upper()

trueNumberOfMatches = 0                                # The number of times a letter in one of the names is also a letter in the word "True"
trueNumberOfMatches += name1UpperCase.count("T")
trueNumberOfMatches += name2UpperCase.count("T")
trueNumberOfMatches += name1UpperCase.count("R")
trueNumberOfMatches += name2UpperCase.count("R")
trueNumberOfMatches += name1UpperCase.count("U")
trueNumberOfMatches += name2UpperCase.count("U")
trueNumberOfMatches += name1UpperCase.count("E")
trueNumberOfMatches += name2UpperCase.count("E")

loveNumberOfMatches = 0                                # The number of times a letter in one of the names is also a letter in the word "Love"
loveNumberOfMatches += name2UpperCase.count("L")
loveNumberOfMatches += name1UpperCase.count("L")
loveNumberOfMatches += name1UpperCase.count("O")
loveNumberOfMatches += name2UpperCase.count("O")
loveNumberOfMatches += name1UpperCase.count("V")
loveNumberOfMatches += name2UpperCase.count("V")
loveNumberOfMatches += name1UpperCase.count("E")
loveNumberOfMatches += name2UpperCase.count("E")

score = trueNumberOfMatches * 10 + loveNumberOfMatches
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

