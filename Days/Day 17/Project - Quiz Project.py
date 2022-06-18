# This is a program I made following Udemy's Day 17 of 100 Days of Code
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/quiz-game-start
#   https://replit.com/@appbrewery/quiz-game-final (Solution)
#   https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean (question pool used)
# Requirements:
#   question_model: Create a Question class with an __init()__ method with two attributes: text and answer attribute
#   Write a for loop to iterate over the question_data
#   Create a Question object from each entry in question_data
#   Append each Question object to the question bank
#   quiz_brain: Asking the Questions
#   quiz_brain: Checking if the answer was correct
#   quiz_brain: Checking if we're at the end of the quiz

# class Question:
#     def __init__(self, text, answer):
#         self.text = "2+3=5"
#         self.answer= "True"
# new_q = Question("2+3=5", "True")
from question_model import Question
from QuizData import question_data
from quiz_brain import QuizBrain

# Challenge:
#   Write a for loop to iterate over the question_data
#   Create a Question object from each entry in question_data
#   Append each Question object to the question_bank
question_bank = []
questions = question_data[0].get("results")
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_to_add = Question(text=question_text, answer=question_answer)
    question_bank.append(question_to_add)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
