import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
cars = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()

screen.onkeypress(player.goUp, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    scoreboard.showScore()
    cars.createCar()
    cars.moveCars()


    for car in cars.all_cars:
        if car.distance(player) < 22:
            game_is_on = False
            scoreboard.gameOver()

    if player.ycor() > 270:
        player.goBack()
        scoreboard.updateScore()
        cars.fasterCar()

screen.exitonclick()