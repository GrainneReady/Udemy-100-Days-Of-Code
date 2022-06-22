from turtle import Turtle

UP_HEADING = 90
DOWN_HEADING = 270

#   2. Create and move a paddle ✔
#   3. Create another paddle ✔


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(coordinates)
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
