# This program is a direct copy of a program I made following Udemy's Day 4 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364931/overview
# Instructions:
#   You are going to write a program that will mark a spot with an X.
#   In the starting code, you will find a variable called map.
#   This map contains a nested list. When map is printed this is what the nested list looks like:
#   ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
#   In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
#   ['⬜️', '⬜️', '⬜️']
#   ['⬜️', '⬜️', '⬜️']
#   ['⬜️', '⬜️', '⬜️']
#   This is to try and simulate the coordinates on a real map.
#   Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit 
#     is the horizontal row number.
#   First, your program must take the user input and convert it to a usable format.
#   Next, you need to use it to update your nested list with an "x".
# Example Input 1:
#   column 2, row 3 would be entered as:
#   23
# Example Output 1:
#   ['⬜️', '⬜️', '⬜️']
#   ['⬜️', '⬜️', '⬜️']
#   ['⬜️', 'X', '⬜️']
# Example Input 2:
# column 3, row 1 would be entered as:
#   31
# Example Output 2:
#   ['⬜️', '⬜️', 'X']
#   ['⬜️', '⬜️', '⬜️']
#   ['⬜️', '⬜️', '⬜️']
# Submission Result (100%):
#   https://gyazo.com/ac6ef94e11ad076ae2d977d0e7444e9dd

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

columnIndexForX = int(position[0]) - 1
rowIndexForX = int(position[1]) - 1

map[rowIndexForX][columnIndexForX] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")