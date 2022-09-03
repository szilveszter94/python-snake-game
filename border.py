from turtle import Turtle
# draw the borders
class Border:
    def __init__(self):
        self.border = Turtle()
        self.border.hideturtle()
        self.border.speed("fastest")
        self.border.color("orange")
        self.border.pensize(17)
        self.border.penup()
        self.border.goto(-240, 240)
        self.border.pendown()
        self.border.goto(-240, -240)
        self.border.goto(240, -240)
        self.border.goto(240, 240)
        self.border.goto(-240, 240)