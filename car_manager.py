from turtle import Turtle
import random

COLOURS = ["red", "blue", "orange", "yellow", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLOURS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.current_speed)

    def speed_up(self):
        self.current_speed += MOVE_INCREMENT
