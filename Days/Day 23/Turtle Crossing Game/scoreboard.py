from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_number = 0
        self.goto(x=-200, y=200)
        self.update_level()

    def update_level(self):
        self.level_number += 1
        self.clear()
        self.write(f"Level: {self.level_number}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
