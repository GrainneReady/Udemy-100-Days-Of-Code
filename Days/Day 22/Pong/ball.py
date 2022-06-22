from turtle import Turtle

#   4. Create the ball and make it move ✔


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_velocity = 10
        self.y_velocity = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset()
        self.speed("fastest")
        self.move_speed = 0.1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_velocity, self.ycor() + self.y_velocity)

    def wallCollisionCheck(self):
        if self.ycor() <= -280 or self.ycor() >= 280:
            self.y_velocity *= -1
            print("hit!")

# Challenge: Get the ball to increase its speed each time it hits a paddle ✔ (I had originally done this by adjusting the x and y velocities, but the course decided to do this by
#               adjusting the time in the while loop in main.py so now the new version is in sync with the instructors' code)
    def paddleCollisionCheck(self, paddle):
        if self.distance(paddle) < 50 and self.xcor() > 320 or self.distance(paddle) < 50 and self.xcor() < -320:
            self.x_velocity *= -1
            self.move_speed *= 0.9

#   7. Detect when paddle misses ✔
    def outOfBoundsCheck(self, scoreboard):
        """Checks to see if the ball has gone past the paddle, meaning the paddle missed the ball
        If one of the paddles has missed and the ball has gone past, a point will be given to the opposite player
        The ball will then reset to the center of the screen so it can be played with again, but it's x velocity will be multipled by -1

        Args:
            scoreboard (Scoreboard): The scoreboard we wish to add points to
        """
        outOfBounds = False
        if self.xcor() > 380:
            scoreboard.add_left_point()
            outOfBounds = True
        elif self.xcor() < -380:
            scoreboard.add_right_point()
            outOfBounds = True
        if outOfBounds:
            self.x_velocity *= -1
            self.reset()
