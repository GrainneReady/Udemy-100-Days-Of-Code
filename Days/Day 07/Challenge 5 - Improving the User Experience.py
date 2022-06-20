# This program is a direct copy of a program I made following Udemy's Day 7 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Challenge Link:
#   https://replit.com/@appbrewery/Day-7-Hangman-5-Start#main.py
# Instructions:
#   TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#   TODO-2: - Import the stages from hangman_art.py and make error go away.
#   TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#   TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#   TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# Updated Flow Chart:
#   https://i.gyazo.com/741b3f39bd7d2c560153bb5211a3b0f9.png

#Step 5

import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in guessed_letters:
        guessed_letters.extend(guess)
    else:
        print(f"You already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, unfortunately it is not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])