# This program is a direct copy of a program I made following Udemy's Day 7 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Challenge Link:
#   https://replit.com/@appbrewery/Day-7-Hangman-1-Start#main.py
# Instructions:
#   TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#   TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#   TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. 


#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")