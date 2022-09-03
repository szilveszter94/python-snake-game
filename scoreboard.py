from turtle import Turtle

FONT = ("Impact", 20, "normal")
ALIGN = "center"
SCORE = 0


# manage scores
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as self.read_high_score:
            self.high_score = int(self.read_high_score.read())
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 256)
        self.show_score()

    # increase score
    def increase_score(self):
        self.score += 1
        self.show_score()

    # manage the top score
    def show_score(self):
        self.clear()
        if self.score > self.high_score:
            with open("data.txt", mode="w") as self.read_high_score:
                self.read_high_score.write(f"{self.score}")
            with open("data.txt") as self.read_high_score:
                self.high_score = int(self.read_high_score.read())
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", font=FONT, align=ALIGN)

    # reset score
    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as self.read_high_score:
                self.read_high_score.write(f"{self.score}")
        self.score = 0
        self.show_score()
