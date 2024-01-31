from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", FONT)

    def level_up(self):
        self.level += 1
        self.update()
