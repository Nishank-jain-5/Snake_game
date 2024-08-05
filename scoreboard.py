from turtle import Turtle

FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,275)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)


