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
        with open("Days\Day 24\snake_game_updated\data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=SCOREBOARD_X_POS, y=SCOREBOARD_Y_POS)
        self.draw()

    def update(self):
        self.score += 1
        self.draw()

    def draw(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Days\Day 24\snake_game_updated\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.draw()
