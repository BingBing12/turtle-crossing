from turtle import Turtle


class Lanes(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.draw_lanes()

    def draw_lanes(self):
        for lane in range(-200, 220, 40):
            self.goto(300, lane)
            self.pendown()
            self.goto(-300, lane)
            self.penup()
