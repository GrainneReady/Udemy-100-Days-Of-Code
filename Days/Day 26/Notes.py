# +------------------------------------+
# |             Section 26             |
# +------------------------------------+
# | List and Dictionary Comprehensions |
# +------------------------------------+

# This is unique to the python language
# Will cut down on a lot of code we have to write when working with lists and dictionaries

# List Comprehension:
#   Creating a list from a previous list

# For Loop
# numbers = [1, 2, 3]
# new_list = []                   # Using List Comprehension, we can turn these four lines into one
# for n in numbers:               #
#     add_1 = n + 1               #
#     new_list.append(add_1)      #

# new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# Working with Strings
# name = "Angela"
# letter_list = [letter for letter in name]

# Python Sequences
# Lists, Range, String, Tuple.. (all have certain order)

# Challenge: Create a range between 1 and 5, make a list where each of the numbers in the range is doubled
#   Aka, from range(1,5) get list that looks like [2,4,6,8]
# range_doubled_list = [number * 2 for number in range(1, 5)]
# print(range_doubled_list)

# Conditional List Comprehension - Only add new item to list and perform code if condition is met
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [new_item for item in list if test]
# short_names = [name for name in names if len(name) < 5]

# NOTE: When in debug console, you can set/edit the values of variables
#       For VSC, just go to the variables tab in debug console and right click the variable you want to edit and click 'Set Value' (or press F2)

# Challenge: Create a new list that contains the names longer than 5 characters in ALL CAPS
#               Result should be: ["CAROLINE", "ELEANOR", "FREDDIE"]
# long_capitalised_names = [name.upper() for name in names if len(name) >= 5]

import random
# Dictionary Comprehensions
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test} # Conditional
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {new_key: new_value for item in list}
# student_scores = {student: random.randint(0, 101) for student in names}
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

# How to Iterate over a Pandas DataFrame
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping through Dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)

# Loop through rows of a data frame <= More ideal than previous method
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    if row.student == "Angela":
        print(row.score)
