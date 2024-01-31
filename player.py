from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.left(90)
        self.position_player()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def position_player(self):
        self.goto(STARTING_POSITION)
