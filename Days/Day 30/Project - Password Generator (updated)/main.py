# This is a program I worked on following Udemy's Day 30 of 100 Days of Code (Instructor-Led Course)
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ------------------------------- FIND PASSWORD ---------------------------------- #
# CHALLENGE: Add a "Search" button next to the website entry field. ✔
#            Adjust the layout and the other widgets as needed to get the desired look. ✔
#            Create a function called find_password() that gets triggered when the "Search" button is pressed. ✔
#            Check if the user's text entry matches an item in the data.json. ✔
#            If yes, show a messagebox with the website's name and password. ✔
#            Catch an exception that might occur trying to access the data.json showing a messagebox with the text: "No Data File Found". ✔
#            If the user's website does not exist inside the data.json, show a messagebox that reads "No details for the website exists." ✔


def find_password():
    website = website_entry.get()
    try:
        with open("Days\\Day 30\\Project - Password Generator (updated)\\data.json", 'r') as save_file:
            data = json.load(save_file)  # Read old data
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            website_dict = data[website]
            messagebox.showinfo(title=website, message=f"Email: {website_dict['email']}\nPassword: {website_dict['password']}")
        else:
            messagebox.showinfo(title=website, message="No details for the website exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# CHALLENGE: Change the existing for loops to use Python List COmprehension instead (see Day 26). ✔
#            Remember to combine the results so that you can shuffle them to create a password. ✔


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
# CHALLENGE: Modify the code to handle the FileNotFoundError/ ✔
#            Create a new data.json file if it does not exist ✔
#            If the file already exists, then simply add the new entry ✔


def save():
    website = website_entry.get()
    email_or_username = email_and_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_or_username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("Days\\Day 30\\Project - Password Generator (updated)\\data.json", 'r') as save_file:
                data = json.load(save_file)  # Read old data
                data.update(new_data)   # Update old data with new data
        except FileNotFoundError:
            with open("Days\\Day 30\\Project - Password Generator (updated)\\data.json", 'w') as save_file:
                json.dump(new_data, save_file, indent=4)
        else:
            with open("Days\\Day 30\\Project - Password Generator (updated)\\data.json", 'w') as save_file:
                json.dump(data, save_file, indent=4)  # Save updated data
        finally:
            password_entry.delete(0, last=len(password))
            website_entry.delete(0, last=len(email_or_username))


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

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
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

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()
