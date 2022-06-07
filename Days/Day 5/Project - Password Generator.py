# This program is a direct copy of a program I made following Udemy's Day 5 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/password-generator-start
# Instructions:
#   None given. Create a password generator.
# Personal Notes:
# random.shuffle() will shuffle the order of a list, this could also be done by creating a new list, choosing an index from the old list at random, adding the element
#   at the chosen index to the new list, and removing said element from the old list until there are no remaining elements in the old list.

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# This will generate a password where the order is not randomised
password = []
generatedCharacter = ''
for letter in range(0, nr_letters):
    generatedCharacter = letters[random.randint(0, len(letters)-1)]
    password.append(generatedCharacter)
for symbol in range(0, nr_symbols):
    generatedCharacter = symbols[random.randint(0, len(symbols) - 1)]
    password.append(generatedCharacter)
for number in range(0, nr_numbers):
    generatedCharacter = numbers[random.randint(0, len(numbers) - 1)]
    password.append(generatedCharacter)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# This will then randomize the order of the password that was previously generated
random.shuffle(password)
print(password)