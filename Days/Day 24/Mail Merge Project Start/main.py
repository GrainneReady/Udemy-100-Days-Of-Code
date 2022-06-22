#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
DEFAULT_MESSAGE = "[name]"
with open("Days\\Day 24\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as namesFile:
    # names = namesFile.read().split("\n") (Original Way I did this, program had the same output, but also decided to include the Instructor's method as they teach new things like readlines() and strip())
    names = namesFile.readlines()
with open("Days\\Day 24\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as startingLetterFile:
    defaultLetter = startingLetterFile.read()
letters = []
for name in names:
    stripped_name = name.strip()
    new_letter = defaultLetter.replace(DEFAULT_MESSAGE, stripped_name)
    with open(f"Days\\Day 24\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode="w") as new_letter_file:
        new_letter_file.write(new_letter)
