# This program is a direct copy of a program I made following Udemy's Day 5 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Assignment Link:
#   https://app.codingrooms.com/management/assignments/364934/overview
# Instructions:
#   You are going to write a program that calculates the highest score from a List of scores.
#     e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#   Important you are not allowed to use the max or min functions. The output words must match the example. i.e
#   The highest score in the class is: x
# Example Input:
#   78 65 89 86 55 91 64 89
# Example Output:
#   The highest score in the class is: 91
# Submission Result (100%):
#   https://i.gyazo.com/b94ecd0ecfa68a0cc8a55c8a202df5d0.png
# Personal Notes:
#   In normal circumstances, it would be useful to use max() to solve this problem.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")