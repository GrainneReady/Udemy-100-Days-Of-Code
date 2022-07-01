import datetime as dt
import smtplib
import pandas
from random import choice

GMAIL_EMAIL = "[insert email here]"
YAHOO_EMAIL = "[insert email here]"
GMAIL_PASSWORD = "[insert password here]"
YAHOO_PASSWORD = "[insert password here]"

# CHALLENGE: Send a motivational quote via email on the current weekday (can change to Monday afterwards) ✔
MONDAY_INDEX = 0
with open("Days\\Day 32\\Project - Birthday Wisher\\quotes.txt") as quotes_data:
    quotes_list = quotes_data.readlines()
now = dt.datetime.now()
if now.weekday() == MONDAY_INDEX:
    quote = choice(quotes_list)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=YAHOO_EMAIL, msg=f"Subject:Motivational Quote of the Day\n\n{quote}")
