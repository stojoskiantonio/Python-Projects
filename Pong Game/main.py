from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time
WIDTH = 800
HEIGHT = 600


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)


paddleLeft = Paddle()
paddleLeft.setPosRight()
paddleRight = Paddle()
paddleRight.setPosLeft()


ball = Ball()

scoreboard = Scoreboard()
screen.listen()


screen.onkeypress(paddleRight.goUp, "Up")
screen.onkeypress(paddleRight.goDown, "Down")

screen.onkeypress(paddleLeft.goUp, "w")
screen.onkeypress(paddleLeft.goDown, "s")
gameOn = True
while gameOn:
    time.sleep(ball.ballSpeed)
    screen.update()
    ball.ballMove()
    ball.ball_down()
    scoreboard.update()

    #Collision with right paddle
    if ball.distance(paddleRight) < 50 and ball.xcor() > 320:
        ball.bounceX()
        #Ball speed increased


    if ball.distance(paddleLeft) < 50 and ball.xcor() < -320:
        ball.bounceX()
        #Ball speed increased


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.leftScore()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rightScore()



#Keep the screen up
screen.exitonclick()