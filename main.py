from turtle import Turtle, Screen

juan = Turtle()
screen = Screen()


def move_forward():
    juan.forward(10)


def move_backward():
    juan.backward(10)


def move_right():
    juan.right(10)


def move_left():
    juan.left(10)


def back_to_start():
    juan.up()
    juan.clear()
    juan.home()
    juan.down()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="c", fun=back_to_start)
screen.exitonclick()
