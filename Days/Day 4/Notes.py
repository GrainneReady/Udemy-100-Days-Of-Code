# Section 4 - Randomisation and Python Lists

# Python uses the Mersenne Twister pseudorandom number generator.

# This video from Khan Academy explains Pseudorandom number generators quite well
#   https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

# askpython.com for documentation

#randint(a, b) returns a random integer between a and b (both incluses). Will raise a ValueError if a > b
# More info here:
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# A Module is like a function in java

import random
#import my_module

random_integer = random.randint(1, 10)

print(random_integer)

#print(my_module.pi)

# Generating Random floating point numbers
# random.random() -> Returns the next random floating point number between [0.0 to 1.0)

random_float = random.random()
print(random_float)

# We can expand the range of random.random() by multiplying the result, e.g. for range [0.0 to 5.0) we multiply by 5
random_float2 = random.random() * 5
print(random_float2)

total_score = random.randint(1, 100)
print(f"The total score is {total_score}%")

# A list is a data structure, which is what you can use to store data in python
fruits = ["Cherry", "Apple", "Pear"]
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
# The order of a list is not lost. Delaware will always be at index 0, Pennsylvania will always be at index 1 UNLESS we manipulate our list

# Print out the first state to join the US
print(states_of_america[0])

# Print out the last state in the list that joined the US
print(states_of_america[-1])

# Changes spelling of Pennsylvania to Pencilvania
states_of_america[1] = "Pencilvania"

# Adds Hawaii to list
states_of_america.append("Massachusetts")

# Data Structures Documentation
# https://docs.python.org/3/tutorial/datastructures.html

# Adds additional list to states of america
states_of_america.extend(["Maryland", "South Carolina", "New Hampshire"])
print(states_of_america)

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Nested list containing both fruits and vegetables
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(fruits[-5])