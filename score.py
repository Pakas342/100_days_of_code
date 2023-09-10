from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 220)
        self.print_scoreboard()

    def print_scoreboard(self):
        self.write(arg=f"{self.left_score} {self.right_score}", align=ALIGNMENT, font=FONT)

    def scored(self, side):
        if side == "left":
            self.left_score += 1
        if side == "right":
            self.right_score += 1
        self.clear()
        self.print_scoreboard()

    def game_over(self):
        if self.left_score == 7 or self.right_score == 7:
            return True

    def winner(self):
        if self.left_score > self.right_score:
            self.goto(0, 0)
            self.write(arg=f"Left wins!", align=ALIGNMENT, font=FONT)
        else:
            self.goto(0, 0)
            self.write(arg=f"Right wins!", align=ALIGNMENT, font=FONT)