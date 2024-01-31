from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

playing = True

screen.onkey(player.move, "Up")

while playing:
    carManager.create_car()
    carManager.move_cars()

    for car in carManager.all_cars:
        if player.distance(car) < 20:
            playing = False
            scoreboard.game_over()

    if player.at_finish():
        player.position_player()
        carManager.speed_up()
        scoreboard.level_up()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
