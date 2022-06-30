# This program is to do with Udemy's Day 30 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022 (Instructor-led Course)
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/365280/overview
#   https://replit.com/@appbrewery/day-30-2-exercise
# Instructions:
#   We've got some buggy code, try running the code.
#   The code will crash and give you a KeyError.
#   This is because some of the posts in the facebook_posts don't have any "Likes".
#   https://cdn.fs.teachablecdn.com/u1humLqATmXKtN2Uec9A
#   Use what you've learnt about exception handling to prevent the program from crashing.
# Submission Result (100%)
#   https://i.gyazo.com/215f38edc703ec0096931d0b1691459b.png

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)
