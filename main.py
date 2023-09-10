import time
import turtle as t
import player_racket as pr
from ball import Ball
from score import Score

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

left_paddle = pr.Racket("left")
right_paddle = pr.Racket("right")
game_ball = Ball()
score = Score()
screen.update()
screen.listen()

screen.onkeypress(fun=left_paddle.go_up, key="w")
screen.onkeypress(fun=left_paddle.go_down, key="s")
screen.onkeypress(fun=right_paddle.go_up, key="Up")
screen.onkeypress(fun=right_paddle.go_down, key="Down")


game_over = False

while not game_over:
    screen.update()
    game_ball.live_ball()
    ball_x_cor = game_ball.xcor()
    # detect collision with ceil and floor
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()

    # detect points:
    if ball_x_cor > 350:
        score.scored("left")
        game_ball.restart("left")
        time.sleep(0.5)
        game_over = score.game_over()
        left_paddle.restart()
        right_paddle.restart()
    if ball_x_cor < -350:
        score.scored("right")
        game_ball.restart("right")
        time.sleep(0.5)
        game_over = score.game_over()
        left_paddle.restart()
        right_paddle.restart()
    # detect collision with paddles
    if (ball_x_cor > 320 and game_ball.distance(right_paddle) < 50) or (ball_x_cor < -320 and game_ball.distance(left_paddle) < 50):
        game_ball.bounce_x()

score.winner()





















screen.exitonclick()