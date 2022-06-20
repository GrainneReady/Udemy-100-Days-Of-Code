# This program is a direct copy of a program I made following Udemy's Day 9 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/364948/overview
# Instructions:
#   You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
#   Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names
#     for keys and their grades for values. The final version of the student_grades dictionary will be checked.
#   DO NOT modify lines 1-7 to change the existing student_scores dictionary.
#   DO NOT write any print statements.
#   This is the scoring criteria:
#   Scores 91 - 100: Grade = "Outstanding"
#   Scores 81 - 90: Grade = "Exceeds Expectations"
#   Scores 71 - 80: Grade = "Acceptable"
#   Scores 70 or lower: Grade = "Fail"
# Expected Output:
#   {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# Submission Result (100%)
#   https://i.gyazo.com/02764fc9fa83c8a95473c200e0434243.png

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    percentage = student_scores[student]
    if percentage <= 70:
        student_grades[student] = "Fail"
    elif percentage <= 80:
        student_grades[student] = "Acceptable"
    elif percentage <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

    

# 🚨 Don't change the code below 👇
print(student_grades)