from turtle import Turtle


# CONSTANT
STARTING_COR = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_square = []
        self.create_snake()
        self.head = self.all_square[0]

    def create_snake(self):
        for position in STARTING_COR:
            self.add_square_in_snake(position)
            

    def add_square_in_snake(self, position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.all_square.append(turtle)

    def extend_snake(self):
        self.add_square_in_snake(self.all_square[-1].position())

    def move(self):
        for square in range(len(self.all_square)-1, 0, -1):
            # follow the path of first square
            newx = self.all_square[square-1].xcor()
            newy = self.all_square[square-1].ycor()
            self.all_square[square].goto(newx,newy)

        self.all_square[0].forward(MOVE_DISTANCE)

    def up(self):
        # change direction of first sqare
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # change direction of first sqare
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        # change direction of first sqare
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        # change direction of first sqare
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # snake collide with wall
    def strike_wall(self):
        if self.head.xcor() >= SCREEN_WIDTH/2 or self.head.xcor() <= -(SCREEN_WIDTH/2) or self.head.ycor() >= (SCREEN_HEIGHT/2) or self.head.ycor() <= -(SCREEN_HEIGHT/2):
            return True
        else:
            return False
        
    # snake colliode with own's tail
    def strike_with_tail(self):
        # use slicing to avoid head (first square) from list to itterate through loop
        for square in self.all_square[1:] :
            if self.head.distance(square) < 10:
                return True
        
        return False
        

