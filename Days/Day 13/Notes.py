# * Like most of my notes, parts of this code was taken from the Day 13 starting repl *
#   https://replit.com/@appbrewery/day-13-start
# Section 13 - Debugging 🐛
#   The process of removing bugs from your code
# First documented bug was found by Grace Hopper, found a moth in a relay which was preventing code from running properly
# Everyone gets bugs, but in a methaphorical sense, not a literal sense.

# https://emojipedia.org/ - Copy and Paste emojis

# Step 1. Describe the Problem 📋✍️
#   If you don't understand it in your head, its almost impossible to debug it
#   Can't solve a problem without knowing what the problem is in the first place, self explanatory?

# Step 2. Reproduce the Bug 🗺️📍
#   Figure out where the bug does occur, and where it does not occur.
#   This helps to figure out which piece of your code this bug occurs in, which will lead you to debug it faster.

# Step 3. Play Computer 🖥️
#   Imagine yourself as being the computer carrying out the code, step by step.
#   Can make it easier to spot why code is not working the way you want to, whether it be from forgotten cases or something else.

# Step 4. Fix the Errors 🛠️
#   If there is a syntax or build error, fix them. Quite obvious.

# Step 5. Print is your Friend 🖨️
#   If it is something as simple as accidentally comparing a variable instead of declaring it, printing your variables will help you figure this out.
#   Among in other cases.
#   You'll only really need to use print when your debugger is not reliable (Remember processing's bad debugger from programming project in Junior Freshman 😠)

# Step 6. Use a Debugger 🐛🥅
#   The best way to debug your code, its purpose is self explanatory. If you're lucky enough to be using an IDE with a working debugger, use it!

# Step 7. Take a Break ☕
#   Sometimes taking soem downtime for 15 minutes or leaving it until tomorrow until you have a fresher mind helps.

# Step 8. Ask a Friend 🧑‍🔧
#   Find other students, or a developer friend. They have fresh eyes to check the code and might spot something you can't see

# Step 9. Run Often 🏃‍♀️
#   Do everything step by step, and run more often so you can see where issues occur easier, instead of waiting until last minute to run and have 5 different issues.

# Step 10. Stack Overflow
#   This should only be done when you've exhausted all other avenues. Check if your issue has already been posted before making a new post.

############DEBUGGING#####################
# We will uncomment the following code blocks one by one and debug them

# Describe Problem
#def my_function():
#  for i in range(1, 21):    # Original Line: for i in range(1, 20):
#    if i == 20:             # This won't print in original, as the code will only go up to 19. Range maximum has to be maxNumber + 1.
#      print("You got it")
#my_function()

# Reproduce the Bug - Issue is IndexError: List Index out of Range, difficult to spot as it won't happen all the time, only when the randint selects the out of range index
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)    # Original Line: dice_num = randint(1, 6), typical mistake, where they started counting from 1 instead of 0 for a list index.
#print(dice_imgs[dice_num])

# Play Computer - Typical mistake where the case where year = 1994 is left out.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:  # Original: elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you?")) # Original Line: age = input("How old are you?"), did not cast to type int which caused TypeError.
# if age > 18:
#     print(f"You can drive at age {age}.")    # Original Line: print("You can drive at age {age}.") Causing indentation error and TypeError. f was left out of print.

#Print is Your Friend - ISSUE: == instead of = in words_per_page
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))   # Original Line: word_per_page == int(input("Number of words per page: ")), comparison not a declaration. (==) instead of (=)
# print(pages)            # Used for debug as requested   
# print(word_per_page)    # Used for debug as requested
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger - ISSUE: Only one item in list
# Online Debugger Recommended by Course: https://pythontutor.com/visualize.html#mode=edit
# (instead I just use Visual Studio Code's included debugging feature, as its my IDE.)
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)       # Indentation fail, Original Line: '  b_list.append(new_item)', should have 4 spaces instead of 2.
  print(b_list)
  
mutate([1,2,3,5,8,13])