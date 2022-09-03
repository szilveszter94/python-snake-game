from turtle import Turtle

FONT2 = ("Impact", 8, "normal")


class Instructions:
    # show the instructions
    def __init__(self):
        self.instructor = Turtle()
        self.instructor.penup()
        self.instructor.hideturtle()

    def instructions(self):
        self.instructor.goto(-290, 220)
        self.instructor.write(arg="INSTRUCTIONS:\n UP - W\nLEFT - A\nDown - S\nRIGHT - D", font=(FONT2))
