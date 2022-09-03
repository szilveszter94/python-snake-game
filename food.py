from turtle import Turtle
import random


# draw a food object to a random position
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(random_x, random_y)
