from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20,0), (-40,0)]
MOVE_SPEED = 20
Up = 90
Down = 270
Right = 0
Left = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segments = Turtle("square")
            new_segments.color("white")
            new_segments.penup()
            new_segments.goto(position)
            self.segments.append(new_segments)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_SPEED)

    def Up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def Down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def Left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def Right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)