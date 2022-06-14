# This program is a direct copy of a program I made following Udemy's Day 12 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/guess-the-number-final#main.py (Solution)
# Notes:
#   http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 is a useful website for getting ASCII logos
#   The lecturer's project does not allow the user to have multiple consecutive games, I've added this feature to my program myself.
#   The constants can be adjusted and the program will work in respect to the adjusted changes.
# Instructions:
#   No typed instructions were given, instead, there was a walkthrough in the lectures.

import random
import os
from NumberGuessingGameArt import logo

EASY_DIFFICULTY_ATTEMPTS = 10
HARD_DIFFICULTY_ATTEMPTS = 5
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100

def difficultySelector():
    """Selects a difficulty of a game based on if the user types 'easy' or 'hard'.
    The difficulty here controls the number of attempts.
    If the user chooses the 'hard' difficulty, this will return the number of attempts in respect to the hard difficulty, otherwise,
    it will return the number of attempts in respect to the easy difficulty.
    To rephrase, If the user fails to type either 'easy' or 'hard', it will give them the easy number of attempts

    Returns:
        int: number of attempts given to user based on what difficulty they chose.
    """
    Difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if Difficulty == "hard":
        return HARD_DIFFICULTY_ATTEMPTS
    else:
        return EASY_DIFFICULTY_ATTEMPTS
    
def guessingGame(number, attemptsLeft):
    """Plays a Number Guessing Game with the user, where they have to guess the parameterized number before they run out of attempts (attemptsLeft).
    It will give hints such as their current guess being "Too high." or "Too low." until they eventually either guess the number or run out of attempts.

    Args:
        number (int): The number the user has to guess.
        attemptsLeft (int): The amount of chances the user has to guess the number.

    Returns:
        String: "You guessed correctly" if guessed number correctly, or "You've run out of guesses, you lose." if they failed to guess correctly and their attempts have run out.
    """
    attempts = attemptsLeft
    while (attempts != 0):
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        guess = int(input("Make a guess: "))
        if guess > generatedNumber:
            print("Too high.")
        elif guess < generatedNumber:
            print("Too low.")
        elif guess == generatedNumber:
            return f"You got it! The answer was {number}."
        if attempts != 0:
            print("Guess again.")
    return "You've run out of guesses, you lose."
        

while input("Do you want to play a Number Guessing Game? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    generatedNumber = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}.")
    attemptsLeft = difficultySelector()
    print(guessingGame(number=generatedNumber, attemptsLeft=attemptsLeft))
    


    