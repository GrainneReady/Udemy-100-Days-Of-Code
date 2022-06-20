# This program is a direct copy of a program I made following Udemy's Day 4 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/rock-paper-scissors-start#README.md
# Instructions:
#   Make a rock, paper, scissors game.
#   Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.
#   Start the game by asking the player:
#   "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
#   From there you will need to figure out:
#   How you will store the user's input.
#   How you will generate a random choice for the computer.
#   How you will compare the user's and the computer's choice to determine the winner (or a draw).
#   And also how you will give feedback to the player.
#   You can find the "official" rules of the game on the World Rock Paper Scissors Association website.
# Personal Notes:
#   0 beats 2
#   2 beats 1
#   1 beats 0
#   Otherwise draw

import random

rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
movesAscii = [rock, paper, scissors]
movesIndexes = [0, 1, 2]

computerMoveChosen = random.randint(0, 2)
userMoveChosen = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if userMoveChosen >= 0 and userMoveChosen <= 2:
    userMoveIndex = movesIndexes.index(userMoveChosen)
    print(movesAscii[userMoveIndex])
    print(f"Computer Chose:\n {movesAscii[computerMoveChosen]}")
    if userMoveChosen == computerMoveChosen:
        print("You Draw!")
    elif movesIndexes[userMoveChosen - 1] == movesIndexes[computerMoveChosen]:
        print("You Win!")
    else:
        print("You Lose!")
else:
    print("You typed an invalid number, you lose!")
