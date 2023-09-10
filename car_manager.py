from turtle import Turtle
import random as r

CAR_COLORS = ["orange", "red", "blue", "black", "purple", "yellow", "brown"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.moving_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for i in range(0, 20):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(r.choice(CAR_COLORS))
            x_position = r.randint(-300, 300)
            y_position = r.randint(-250, 250)
            new_car.goto(x=x_position, y=y_position)
            self.cars.append(new_car)

    def restart_car(self, car_to_restart):
        new_y_position = r.randint(-250, 250)
        car_to_restart.goto(x=300, y=new_y_position)

    def move(self):
        for car in self.cars:
            car.goto(x=car.xcor() + (self.moving_distance * -1), y=car.ycor())

    def next_level(self):
        self.moving_distance += SPEED_INCREMENT
