# This program is a direct copy of a program I made following Udemy's Day 4 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364927/overview
# Instructions:
#   You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#   Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#   When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.
#   There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
#   e.g. 1 means Heads 0 means Tails
# Example Output:
#   Heads
# Example Output 2:
#   Tails
# Submission Result (100%):
#   https://i.gyazo.com/0c9d1e15eb2aa5590df7303d4c34ece5.png
# Personal Notes:
#   seed() initializes a random number generator.
#   Since pseudorandom generation is based on the previous number, we often use the system time to make sure that the program gives a new output
#    every time we run it. The seed value determines the output of the random number generator
#   Its easier to think of it like a regular input and output, the seed is the input, and it can only have one output. 
#   For example, if the seed is 10 in this program, then the coin will always land on tails.

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

coinFlip = random.randint(0, 1)
if coinFlip == 1:
    print("Heads")
else:
    print("Tails")
