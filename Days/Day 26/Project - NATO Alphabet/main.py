# This is a program I worked on while following Udemy's Day 26 of 100 Days of Code (Instructor-Led Course)
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
#for (key, value) in student_dict.items():
#    # Access key and value
#    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: ✔
# {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv("Days\\Day 26\\Project - NATO Alphabet\\nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs. ✔
word_to_convert = input("Enter a word: ").upper()
word_in_nato_phonetic = [nato_dict[letter] for letter in word_to_convert]
print(word_in_nato_phonetic)
