from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)


    def goUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def goDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)

    def setPosLeft(self):
        self.setposition(340, 0)

    def setPosRight(self):
        self.setposition(-340, 0)