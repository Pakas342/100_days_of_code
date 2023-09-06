from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.print_scoreboard()

    def print_scoreboard(self):
        self.write(arg=f"Puntaje: {self.player_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)


    def user_point(self):
        self.clear()
        self.player_score += 1
        self.print_scoreboard()