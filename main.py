from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PING-PING")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

screen.exitonclick()