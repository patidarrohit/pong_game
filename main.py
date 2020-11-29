from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PongGame")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 325) or (ball.distance(l_paddle) < 50 and ball.xcor() < -325):
        ball.bounce_x()
    # detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()
    # detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
