import turtle as t
from snake import Snake
from food import Food
from score import Score

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

score = Score()
juan = Snake(size=3)
food = Food()
screen.update()
screen.listen()

screen.onkeypress(key="s", fun=juan.go_down)
screen.onkeypress(key="w", fun=juan.go_up)
screen.onkeypress(key="a", fun=juan.go_left)
screen.onkeypress(key="d", fun=juan.go_right)

game_is_om = True
while game_is_om:

    screen.update()
    juan.go_forward()

    # Detect if snake ate food
    if juan.head.distance(x=food.xcor(), y=food.ycor()) <= 15:
        score.user_point()
        food.move()
        juan.grow()

    # Detect if snake hit a wall
    if juan.head.xcor() > 280 or juan.head.xcor() < -280 or juan.head.ycor() > 280 or juan.head.ycor() < -280:
        game_is_om = False
        score.game_over()

    # Detect if snake hit herself
    for part in juan.snake[1:]:
        if juan.head.distance(part) < 10:
            game_is_om= False
            score.game_over()












screen.exitonclick()