# +----------------------------------+
# |            Section 30            |
# +----------------------------------+
# | Errors, Exceptions and JSON Data |
# +----------------------------------+

# Handling Errors & Exceptions

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try: Something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens
# it is bad to have a blank except, should always have the type of error
# We can have multiple exceptions for multiple different errors for the same try statement
# try:
#     file = open("Days\\Day 30\\a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("Days\\Day 30\\a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:  # If there were no exceptions
#     content = file.read()
#     print(content)
# finally:  # Will run no matter what happens
#     raise TypeError("This is an error that I made up")
#     file.close()
#     print("File was closed.")

# raise: Allows us to raise our own exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2

# JSON - JavaScriptObjectNotation
#   Composed of nested lists and dictionaries
#   Key: Value pair data structure

# write
# json.dump()

# read
# json.load()

# update
# json.update()
