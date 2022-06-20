# This program is a direct copy of a program I made following Udemy's Day 8 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://replit.com/@appbrewery/caesar-cipher-3-start#main.py
# Instructions:
#   TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#   TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values. 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
    if direction.lower() == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction.lower() == "decode":
        decrypt(cipher_text=text, shift_amount=shift)
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

#if direction == "encode":
#  encrypt(plain_text=text, shift_amount=shift)
#elif direction == "decode":
#  decrypt(cipher_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift=shift, direction=direction)