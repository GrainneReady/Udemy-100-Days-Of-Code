from turtle import Turtle

# Challenge: Create a scoreboard class which will inherit from Turtle. It should keep track of score and be able to display it in our program ✔

SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 270
ALIGNMENT = "CENTER"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=SCOREBOARD_X_POS, y=SCOREBOARD_Y_POS)
        self.draw()

    def update(self):
        self.score += 1
        self.clear()
        self.draw()

    def draw(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
