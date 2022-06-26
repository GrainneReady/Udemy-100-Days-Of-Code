from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
# Picked colours from https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WORK_SECONDS = 1500
SHORT_BREAK_SECONDS = 300
LONG_BREAK_SECONDS = 1200
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    current_stage_lable["text"] = ""
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
# CHALLENGE: Make it so that if it is the 8th rep, the clock will count down a long break ✔
#            If it is the 2nd, 4th, 6th, ... , etc. rep, the clock will count down a short break ✔
#            If it is the 1st, 3rd, 5th, ... , etc. rep, the clock will count down the time for work ✔
#            (I also added functionality so that this can work for longer than just 8 reps, it can go continuously)
# CHALLENGE: During a long break, update the label to "Break" in red. ✔
#            During a short break, update the label to "Break" in pink. ✔
#            During work time, update the label to "Work" in green. ✔


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_SECONDS)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_SECONDS)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_SECONDS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes_left = floor(count / 60)
    seconds_left = count % 60
    if seconds_left == 0:  # Dynamic Typing
        seconds_left = "00"
    # CHALLENGE: Make it so that when there are less than 10 seconds left, it will show as 09 or 07 seconds etc. instead of just 9 or 7 ✔
    elif seconds_left < 10:
        seconds_left = f"0{seconds_left}"
    canvas.itemconfig(timer_text, text=f"{minutes_left}:{seconds_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # CHALLENGE: Add one checkmark for every two reps ✔
        if reps % 2 == 0:
            current_stage_lable["text"] = current_stage_lable["text"] + "✔"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Days\\Day 28\\Project - Pomodoro\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

current_stage_lable = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16))
current_stage_lable.grid(column=1, row=3)

window.mainloop()
