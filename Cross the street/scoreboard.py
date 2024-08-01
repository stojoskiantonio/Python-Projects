FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("Black")
        self.hideturtle()

    def showScore(self):
        self.goto(0, 260)
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def updateScore(self):
        self.clear()
        self.score += 1
        self.showScore()

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over, your final score was {self.score}", align="center", font=("Courier", 14, "normal"))


