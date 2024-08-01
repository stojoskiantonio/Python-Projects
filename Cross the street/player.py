STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('green')
        self.setposition(STARTING_POSITION)
        self.shape('turtle')
        self.setheading(90)


    def goUp(self):
        self.forward(MOVE_DISTANCE)

    def goDown(self):
        self.forward(-10)

    def goBack(self):
        self.goto(STARTING_POSITION)