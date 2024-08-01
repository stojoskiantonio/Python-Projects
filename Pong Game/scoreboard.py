FONT = ('Arial', 25, 'bold')
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.hideturtle()
        self.color('white')

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.lscore}', align='center', font= FONT)
        self.goto(100, 200)
        self.write(f'{self.rscore}', align='center', font= FONT)

    def leftScore(self):
        self.lscore += 1
        self.update()

    def rightScore(self):
        self.rscore += 1
        self.update()
