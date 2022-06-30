# This is a program I worked on following Udemy's Day 29 of 100 Days of Code (Instructor-Led Course)
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# CHALLENGE: Change the existing for loops to use Python List COmprehension instead (see Day 26).
#            Remember to combine the results so that you can shuffle them to create a password.


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    generated_letters = [random.choice(letters) for num in range(random.randint(8, 10))]
    generated_symbols = [random.choice(symbols) for num in range(random.randint(2, 4))]
    generated_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    password_list = generated_letters + generated_symbols + generated_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, last=len(password_entry.get()))
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# CHALLENGE: Create a function called save()
#            Write to the data inside the entries to a data.txt file when the Add button is clicked. ✔
#            Each website, email, and password combination should be on a new line inside the file. ✔
#            All fields need to be cleared after Add button is pressed. ✔
# CHALLENGE: Do not save the data and show the pop up if the website or password fields were left empty. ✔
#            POPUP: title = "Oops", message = "Please don't leave any fields empty!"


def save():
    website_to_save = website_entry.get()
    email_or_username_to_save = email_and_username_entry.get()
    password_to_save = password_entry.get()
    if len(website_to_save) == 0 or len(password_to_save) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_to_save, message=f"These are the details entered: \nEmail: {email_or_username_to_save}\n"
                                       f"Password: {password_to_save}\nIs it ok to save?")
        if is_ok:
            with open("Days\\Day 29\\Project - Password Generator\\data.txt", 'a') as saveFile:
                saveFile.write(f"{website_to_save} | {email_or_username_to_save} | {password_to_save}\n")
            password_entry.delete(0, last=len(password_to_save))
            website_entry.delete(0, last=len(email_or_username_to_save))


# ---------------------------- UI SETUP ------------------------------- #
# NOTE: Had to add sticky parameter to some of the grid methods as the lecturer was using Mac's default font which affected the alignment
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Days\\Day 29\\Project - Password Generator\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_and_username_label = Label(text="Email/Username:")
email_and_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_and_username_entry = Entry(width=35)
email_and_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_and_username_entry.insert(0, "fakeemail@internet.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
