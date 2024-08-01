from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.ballSpeed = 0.1

    def ballMove(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_down(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1
            self.ballSpeed *= 0.9

    def bounceX(self):
        self.x_move *= -1
        self.ballSpeed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.ballSpeed = 0.1

