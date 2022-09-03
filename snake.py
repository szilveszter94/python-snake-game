from turtle import Turtle

POS_SNAKE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        # set variables
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]


    def create_snake(self):
        for i in POS_SNAKE:
            self.add_new_part(i)

    # reset the snake to default position
    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    # increase the snake
    def add_new_part(self, i):
        tom = Turtle("square")
        tom.penup()
        tom.goto(i)
        self.snakes.append(tom)

    def extend(self):
        self.add_new_part(self.snakes[-1].position())
     # moving all snake units
    def move(self):
        for segment_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[segment_num - 1].xcor()
            new_y = self.snakes[segment_num - 1].ycor()
            self.snakes[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
