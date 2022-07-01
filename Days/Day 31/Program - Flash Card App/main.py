# This is a program I worked on while following Udemy's Day 31 of 100 Days of Code (Instructor-Led Course by Dr. Angela Yu)
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/

from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
card_deck = {}
try:
    data = pandas.read_csv("Days\\Day 31\\Program - Flash Card App\\data\\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Days\\Day 31\\Program - Flash Card App\\data\\french_words.csv")
finally:
    card_deck = data.to_dict(orient="records")


def remove_card():
    card_deck.remove(current_card)
    updated_deck = pandas.DataFrame(card_deck)
    updated_deck.to_csv("Days\\Day 31\\Program - Flash Card App\\data\\words_to_learn.csv", index=False)
    next_card()


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(card_deck)
    canvas.itemconfig(card_face, image=card_front_image)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_face, image=card_back_image)
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_back_image = PhotoImage(file="Days\\Day 31\\Program - Flash Card App\\images\\card_back.png")
card_front_image = PhotoImage(file="Days\\Day 31\\Program - Flash Card App\\images\\card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_face = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="Days\\Day 31\\Program - Flash Card App\\images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="Days\\Day 31\\Program - Flash Card App\\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
