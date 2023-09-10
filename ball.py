import turtle as t
import random as r
import time


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_to_go = 10
        self.x_to_go = 10

    def live_ball(self):
        time.sleep(0.03)
        new_x = self.xcor() + self.x_to_go
        new_y = self.ycor() + self.y_to_go
        self.goto(x= new_x, y=new_y)

    def bounce_y(self):
        self.y_to_go = self.y_to_go * -1

    def bounce_x(self):
        self.x_to_go = self.x_to_go * -1
        self.y_to_go = self.y_to_go + r.randint(-5, 5)

    def restart(self,side_to_go):
        self.goto(0, 0)
        if side_to_go == "left":
            self.x_to_go = -10
        if side_to_go == "right":
            self.x_to_go = 10
