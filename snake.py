import turtle as t
import time
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, size):
        self.snake = []
        self.create_snake(size= size)
        self.head = self.snake[0]


    def create_snake(self, size):
        starting_x = 0
        for square in range(size):
            new_square = t.Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(starting_x,0)
            starting_x -= 20
            self.snake.append(new_square)

    def grow(self):
        new_square = t.Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        tail = self.snake[-1]
        tail_x = tail.xcor()
        tail_y = tail.ycor()
        new_square.goto(x=tail_x, y=tail_y)
        self.snake.append(new_square)

    def go_forward(self):
        time.sleep(0.1)
        for seg_num in range(len(self.snake) - 1, 0, -1):
            pos_to_go = (self.snake[seg_num - 1].xcor(), self.snake[seg_num - 1].ycor())
            self.snake[seg_num].goto(pos_to_go)
        self.head.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
