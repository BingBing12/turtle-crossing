from turtle import Screen
import time
import random
from cars import Car
from player import Player
from score import Score
from lanes import Lanes


def move():
    player.cross()


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=500)
screen.listen()
screen.onkey(move, "Up")
score = Score()
lanes = Lanes()
game_on = True
car_speed = 0.2
cars = []
player = Player()
while game_on:
    time.sleep(car_speed)
    screen.update()
    if player.ycor() > 200:
        player.reset()
        car_speed *= 0.8
        score.update()
    for lane in range(-180, 200, 40):
        if random.randint(0, 40) == 1:
            car = Car(lane)
            cars.append(car)
    for car in cars:
        if car.xcor() < -300:
            print(cars[0])
            cars.pop(0)
            print(cars[0])
        elif car.ycor() == player.ycor() and car.distance(player) < 15:
            game_on = False
            score.game_over()
        else:
            car.drive()
screen.exitonclick()
