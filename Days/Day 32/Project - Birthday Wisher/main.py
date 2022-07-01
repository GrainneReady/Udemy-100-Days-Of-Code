# This is a program I worked on while following Udemy's Day 32 of 100 Days of Code (Instructor-Led Course by Dr. Angela Yu)
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/

# ##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv ✔

# 2. Check if today matches a birthday in the birthdays.csv ✔

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv ✔

# 4. Send the letter generated in step 3 to that person's email address. ✔

import datetime as dt
import pandas
from random import choice
import smtplib

GMAIL_EMAIL = "[insert email here]"
GMAIL_PASSWORD = "[insert password here]"

birthdays_data = pandas.read_csv("Days\\Day 32\\Project - Birthday Wisher\\birthdays.csv")
birthdays_dict = birthdays_data.to_dict(orient='records')
letters = []
for currentLetter in range(1, 4):
    with open(f"Days\\Day 32\\Project - Birthday Wisher\\letter_templates\\letter_{currentLetter}.txt") as letter:
        letters.append(letter.read())

todays_date = (dt.datetime.now().month, dt.datetime.now().day)
for birthday in birthdays_dict:
    if todays_date == (birthday["month"], birthday["day"]):
        letter_to_post = choice(letters)
        letter_to_post = letter_to_post.replace("[NAME]", birthday["name"])
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=GMAIL_EMAIL, password=GMAIL_PASSWORD)
            connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=birthday["email"], msg=f"Subject:Happy Birthday!\n\n{letter_to_post}")
