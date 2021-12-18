from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, lane):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(300, lane)
        self.setheading(180)
        self.drive()

    def drive(self):
        self.forward(10)
