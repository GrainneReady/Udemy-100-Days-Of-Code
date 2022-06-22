# +------------------------------------------+
# |                Section 24                |
# +------------------------------------------+
# | Working with Local Files and Directories |
# +------------------------------------------+

# Files
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# with open("Days\Day 24\my_file.txt") as file:   # With open(path) as file prevents the need to close the file at the end of our program
#     contents = file.read()                      # If we didn't want to use with, we would do 'file = open("Days\Day 24\my_file.txt")' and remove indenting
#     print(contents)

# with open("Days\Day 24\my_file.txt", mode="w") as file:  # mode ='w' changes from Read-only mode to Write-only mode
#     file.write("New text.")

with open("Days\Day 24\my_file.txt", mode="a") as file:  # mode ='a' opens file for appending, any data written to the file is automatically added to the end.
    file.write("New text.")


# NOTE: if you try to open a file in write mode, and that file doesn't exist, it will create it for you from scratch.
with open("Days\Day 24\my_new_file.txt", mode="a") as file:
    file.write("New text.")

# Paths
# To get relative file path for item in current folder:
#   ./item.txt
# To get relative file path for item in enclosed folder:
#   ../item.txt

# To get relative file path for item in deeper folder:
#   ./foldername/item.txt

# Read a file from 3 folders less deep than the workspace directory
with open("../../../test.txt") as file:
    print(file.read())

# readLines() reads each line in a file and puts them into a list
# replace(str1, str2) will replace any str1s in a string with str2
# strip() removes spaces at the beginning and end of a string, can also put specific characters we want to remove as leading/trailing characters in the parameter
#   Example: (https://www.w3schools.com/python/ref_string_strip.asp)
#     txt = ",,,,,rrttgg.....banana....rrr"
#     x = txt.strip(",.grt")
#     print(x)
