
#importing turtle module
from turtle import Turtle

# import random module
import random

# inherit turtle class
class Food(Turtle):

    # create (turtle as a food) on screen at random position
    def __init__(self):

        # to invoke turtle class constructor
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.food_on_random_location()

    # shift food on random location on screen
    def food_on_random_location(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)

    