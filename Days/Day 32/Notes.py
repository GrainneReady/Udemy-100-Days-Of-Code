# +------------------------------------+
# |             Section 32             |
# +------------------------------------+
# | Email SMTP and the DateTime Module |
# +------------------------------------+

# Simple Mail Transfer Protocol

# smtplib is a module that comes prebundled with python and allows us to send emails
# DateTime is a module that allows us to figure out the current time, date etc. and how to format dates/time also.

# SMTP Addresses
#   Google: smtp.gmail.com
#   Hotmail: smtp.live.com
#   Outlook: outlook.office365.com
#   Yahoo: smtp.mail.yahoo.com

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # Transport Layer Security - Encrypt email, secures line
#     connection.login(user=gmail_email, password=gmail_password)
#     connection.sendmail(from_addr=gmail_email, to_addrs=yahoo_email, msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()  # NOTE: Counts days from 0 starting on Monday (Tuesday = 1, Thursday = 3, Sunday = 6, etc.)
# print(day_of_week)

# date_of_birth = dt.datetime(year=2022, month=11, day=15, hour=13)
# print(date_of_birth)

# Make sure you've enabled less secure apps if you are sending from Gmail addresses
# Try to go through the Gmail Captcha while logged in to the Gmail Account
#   https://accounts.google.com/DisplayUnlockCaptcha
# Add a port number by changing your code to this:
#   smtplib.SMTP("smtp.gmail.com", port=587)

# Alphabet have changed the way gmail runs, less secure apps is no longer an option so we need to use an app password
# For this we need to:
#   Turn on 2FA
#   Generate new app password in security tab of google account
#   Use app password instead of normal log in password

# Yahoo:
#   Generate app password in security tab, otherwise connection will close

# To use a subject in email:
#   msg="Subject:[Subject text]\n\n[Body text]"

# PythonAnywhere allows you to host, run, and code Python in the cloud
#   https://www.pythonanywhere.com/
