from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 260)
        self.print_scoreboard()

    def print_scoreboard(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.print_scoreboard()

    def game_over(self):
        self.clear()
        self.write(arg=f"GAME OVER level: {self.level}", align=ALIGNMENT, font=FONT)
