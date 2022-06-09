# This program is a direct copy of a program I made following Udemy's Day 8 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://replit.com/@appbrewery/caesar-cipher-1-start#main.py
# Instructions:
#   TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#   TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     e.g. 
#     plain_text = "hello"
#     shift = 5
#     cipher_text = "mjqqt"
#     print output: "The encoded text is mjqqt"
#     HINT: How do you get the index of an item in a list:
#     https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#     #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#   TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

NUMBER_OF_LETTERS_IN_ALPHABET = 26
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(textToEncrypt, shiftAmount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    encryptedMessage = ""
    for i in range(0, len(textToEncrypt)):
        oldIndex = alphabet.index(textToEncrypt[i])
        newIndex = oldIndex + shiftAmount
        if newIndex >= NUMBER_OF_LETTERS_IN_ALPHABET - 1:
            newIndex -= NUMBER_OF_LETTERS_IN_ALPHABET
        encrypedLetter = alphabet[newIndex]
        encryptedMessage += encrypedLetter
    print(f"The encoded text is {encryptedMessage}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(textToEncrypt = text, shiftAmount = shift)