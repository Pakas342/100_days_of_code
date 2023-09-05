from turtle import Turtle, Screen, colormode
import random as r

colormode(255)
screen = Screen()
screen.setup(width=500, height=400)


def random_turtle_color(turtle_to_change):
    turtle_to_change.color((r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))


def go_to_start(turtles_to_race):
    start_x = -230
    max_y = 200
    space = abs(max_y * 2) / len(turtles_to_race)
    print(space)
    start_y = (space / 2) + (space * ((len(turtles_to_race) / 2) - 1))
    print(start_y)
    for turtle in turtles_to_race.values():
        random_turtle_color(turtle)
        turtle.up()
        turtle.goto(x=start_x, y=start_y)
        start_y -= space


def racing_turtles(turtles_names):
    turtles_racing = {}
    for turtle_to_race in turtles_names:
        turtles_racing[turtle_to_race] = Turtle(shape="turtle")
    return turtles_racing


is_race_on = False
new_turtle = True
turtle_names = []
while new_turtle:
    new_turtle = screen.textinput(title="new turtle", prompt="New racing turtle name:")
    turtle_names.append(new_turtle)
    new_turtle = bool(screen.textinput(title="new turtle", prompt="more turtle? '1' for yes, 'blank' for no: "))


turtles_currently_racing = racing_turtles(turtle_names)
go_to_start(turtles_currently_racing)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          f"{turtle_names}?")
while user_bet == "":
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                              f"{turtle_names}?")
is_race_on = True
user_won = False

while is_race_on:
    for turtle_moving in turtles_currently_racing:
        if turtles_currently_racing[turtle_moving].xcor() >= 230:
            print(f"ganó {turtle_moving}")
            is_race_on = False
            if turtle_moving == user_bet:
                user_won = True
        random_distance = r.randint(0, 10)
        turtles_currently_racing[turtle_moving].forward(random_distance)

if user_won:
    print("Ganaste!")
else:
    print("Perdiste :(")

screen.exitonclick()
