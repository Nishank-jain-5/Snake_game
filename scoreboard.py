
# importing turtle module
from turtle import Turtle

# constant
FONT = ("Arial", 15, "normal")

# inherit turtle class
class Scoreboard(Turtle):
    
    # create "score: " on screen (invoke with constructur)
    def __init__(self):
        
        # run constructur in subclass constructor using super keyboard
        # invoke turtle constructor to create turtle on screen as a score
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,275)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    # update scoreboard when snake is coliode with food
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    # game over when snake either hits wall or itself
    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)


