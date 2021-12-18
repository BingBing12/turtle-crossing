from turtle import Screen
import time
import random
from cars import Car
from player import Player


def move():
    player.cross()


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=500)
screen.listen()
screen.onkey(move, "Up")
game_on = True
car_speed = 0.2
cars = []
player = Player()
while game_on:
    time.sleep(car_speed)
    screen.update()
    if player.ycor() > 240:
        player.reset()
        car_speed *= 0.8
    for lane in range(-180, 250, 40):
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
        else:
            car.drive()
screen.exitonclick()
