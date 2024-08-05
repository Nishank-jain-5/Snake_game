from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen ssetup
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("The turtle game")

# remove turtle animation
screen.tracer(0)

# create snake or food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# control snake from keypress
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# game start
game_is_on = True

while game_is_on:
    # add turtle animation
    screen.update()
    # take a break of 0.1 second
    time.sleep(0.1)

    # move snake
    snake.move()

    #collision of food with first square of snake
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        snake.extend_snake()
        scoreboard.update_scoreboard()
        food.food_on_random_location()

    # check snake is striking a wall or not
    if snake.strike_wall() or snake.strike_with_tail():
        game_is_on = False
        scoreboard.game_over()

    
# exit on click from turtle screen
screen.exitonclick()