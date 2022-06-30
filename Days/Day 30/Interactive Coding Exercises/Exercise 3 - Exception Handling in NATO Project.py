import pandas

nato_data_frame = pandas.read_csv("Days\\Day 26\\Project - NATO Alphabet\\nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
# CHALLENGE: Catch the KeyError when a user enters a character that is not in the dictionary. ✔
#            Provide feedback to the user when an illegal word was entered. ✔
#            Continue prompting the user to enter another word until they enter a valid word. ✔


def generate():
    word_to_convert = input("Enter a word: ").upper()
    try:
        word_in_nato_phonetic = [nato_dict[letter] for letter in word_to_convert]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()
    else:
        print(word_in_nato_phonetic)


generate()
