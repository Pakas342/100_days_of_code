# creating a racket:
import turtle as t
import time
MOVE_DISTANCE = 20
MAX_Y_COR = 250
MIN_Y_COR = -240


class Racket(t.Turtle):
    def __init__(self, screen_side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if screen_side == "left":
            self.goto(-350, 0)
        if screen_side == "right":
            self.goto(350, 0)

    def go_up(self):
        if self.ycor() < MAX_Y_COR:
            self.goto(x=self.xcor(), y=(self.ycor() + 20))

    def go_down(self):
        if self.ycor() > MIN_Y_COR:
            self.goto(x=self.xcor(), y=(self.ycor() - 20))

    def restart(self):
        self.goto(x=self.xcor(), y=0)



