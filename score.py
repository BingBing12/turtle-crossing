from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 230)
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center")

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align="center")
        self.goto(0, 210)
        self.write(f"your final score is {self.score}", align="center")
