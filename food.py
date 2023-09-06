from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = r.randint(a=-270, b=270)
        random_y = r.randint(a=-270, b=270)
        self.goto(x=random_x, y=random_y)

    def move(self):
        random_x = r.randint(a=-270, b=270)
        random_y = r.randint(a=-270, b=270)
        self.goto(x=random_x, y=random_y)

