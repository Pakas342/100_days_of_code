import time
import turtle as t
from playing_turtle import CrossingTurtle
from car_manager import CarManager
from score import Score

screen = t.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

all_cars = CarManager()
juan = CrossingTurtle()
score = Score()
screen.update()

# letting the player move the turtle
screen.onkeypress(key="Up", fun=juan.move_up)
screen.onkeypress(key="Down", fun=juan.move_down)
screen.onkeypress(key="Left", fun=juan.move_left)
screen.onkeypress(key="Right", fun=juan.move_right)

game_over = False
while not game_over:
    time.sleep(0.1)
    all_cars.move()
    for car in all_cars.cars:
        if car.xcor() < -300:
            all_cars.restart_car(car)
        x_distance = juan.xcor() - car.xcor()
        if car.distance(juan) < 20:
            game_over = True
            score.game_over()
    if juan.ycor() > 260:
        score.next_level()
        juan.next_level()
        all_cars.next_level()
    screen.update()


screen.exitonclick()
