from turtle import Turtle

LENGTH_OF_SEGMENTS = 20
MOVE_DISTANCE = 20
STARTING_X_POS = 0
STARTING_Y_POS = 0
UP_HEADING = 90
DOWN_HEADING = 270
LEFT_HEADING = 180
RIGHT_HEADING = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for segment_number in range(3):
            self.add_segment((STARTING_X_POS + (segment_number * 20), STARTING_Y_POS))
        self.first_segment = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # (Start = len(self.segments) - 1, Stop = 0, Step = -1)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)    # Segments will go to the position of the previous segment, e.g. segment 2 will teleport to segment 1's position, this helps us turn without losing the body
        self.first_segment.forward(MOVE_DISTANCE)

    def up(self):
        if self.first_segment.heading() != DOWN_HEADING:
            self.first_segment.setheading(UP_HEADING)

    def down(self):
        if self.first_segment.heading() != UP_HEADING:
            self.first_segment.setheading(DOWN_HEADING)

    def left(self):
        if self.first_segment.heading() != RIGHT_HEADING:
            self.first_segment.setheading(LEFT_HEADING)

    def right(self):
        if self.first_segment.heading() != LEFT_HEADING:
            self.first_segment.setheading(RIGHT_HEADING)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
