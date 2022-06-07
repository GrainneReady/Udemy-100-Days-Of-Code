# This program is a direct copy of a program I made following Udemy's Day 5 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364933/overview
# Instructions:
#   You are going to write a program that calculates the average student height from a List of heights.
#     e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#   The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#     e.g.
#       180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#   There are a total of 7 heights in student_heights
#     1146 ÷ 7 = 163.71428571428572
#   Average height rounded to the nearest whole number = 164
#   Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops. 
# Example Input:
#   156 178 165 171 187
# Example Output:
#   171
# Submission Result (100%):
#   https://i.gyazo.com/c677c3dad028d6127926fc3514ca44cb.png
# Personal Notes:
#   In normal circumstances, it would be useful to use sum() and/or len() to solve this problem.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

numberOfHeights = 0
sumOfHeights = 0
for height in student_heights:
    numberOfHeights += 1
    sumOfHeights += height
averageHeight = round(sumOfHeights / numberOfHeights)

print(averageHeight)
