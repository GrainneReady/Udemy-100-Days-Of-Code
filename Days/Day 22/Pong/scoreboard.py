from turtle import Turtle

#   8. Keep Score ✔


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def add_left_point(self):
        """Adds a point to the score of the left paddle
        """
        self.left_score += 1
        self.update()

    def add_right_point(self):
        """Adds a point to the score of the right paddle
        """
        self.right_score += 1
        self.update()

    def update(self):
        """Clears and then rewrites the current scores
        """
        self.clear()
        self.goto(-100, 210)
        self.write(self.left_score, align="center", font=("Courier", 64, "normal"))
        self.goto(100, 210)
        self.write(self.right_score, align="center", font=("Courier", 64, "normal"))
