# This is a program I made following Udemy's Day 27 of 100 Days of Code (Instructor-Led Course)
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/

from tkinter import *


def miles_to_kilometers():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609, 2)
    calculated_kilometers_label.config(text=f"{kilometers}")


window = Tk()
window.title(string="Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

calculated_kilometers_label = Label(text="0")
calculated_kilometers_label.grid(column=1, row=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(column=1, row=2)

window.mainloop()
