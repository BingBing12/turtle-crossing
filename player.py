from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0, -220)

    def cross(self):
        self.forward(40)

    def reset(self):
        self.goto(0, -220)
