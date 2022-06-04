# This program is made following Udemy's Day 3 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#      https://www.udemy.com/course/100-days-of-code/
# Preview URLs:
#   https://i.gyazo.com/34430d7b68a90371f9599043955b16fb.png
#   https://replit.com/@appbrewery/treasure-island-start
#   https://replit.com/@appbrewery/treasure-island-end (Solution)
# Instructions:
#   Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.
#   To write your code according to my story, you can use this flow chart from draw.io to help you.
#   However, I think the fun part is writing your own story 😊
#   🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀
#   That said if you'd like to continue with my example, feel free to use the text snippets below...
#   Text Snippets from my example
#   'You're at a crossroad. Where do you want to go? Type "left" or "right"'
#   'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
#   "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
#   "It's a room full of fire. Game Over."
#   "You found the treasure! You Win!"
#   "You enter a room of beasts. Game Over."
#   "You chose a door that doesn't exist. Game Over."
#   "You get attacked by an angry trout. Game Over."
#   "You fell into a hole. Game Over."
# Example Input:
#
# Example Output:
#   
# Personal Notes:
#  using .lower() is useful when we want to be case insensitive

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#Write your code below this line 👇

crossRoadTurn = input("You're at a crossroads, where do you want to go? Type \"left\" or \"right\"").lower()
if crossRoadTurn == "left":
    lakeTurn = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.").lower()
    if lakeTurn == "wait":
        colourChosen = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if colourChosen == "red":
            print("It's a room full of fire. Game Over.")
        elif colourChosen == "yellow":
            print("You found the treasure! You Win!")
        elif colourChosen == "blue":
            print("You opened the door and were immediately greeted by a pack of hungry lions. They didn't take too kindly to your interruption and pounced on you immediately. Game Over. ")
        else:
            print("You chose a door that doesn't exist, panicked, and fell off the edge of the world. Game Over")
    else:
        print("You start swimming in the lake, and were attacked by a shoal of piranhas. Game Over")
else:
    print("You fell into a hole. Game Over.")
        