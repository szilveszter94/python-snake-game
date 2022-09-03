from turtle import Screen
import time
from instructions import Instructions
from border import Border
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setting speed 0.1 fastest, 0.9 slowest speed
SNAKE_SPEED = 0.1

screen = Screen()
# screen configuration
screen.setup(width=600, height=600)
screen.bgpic("snake.gif")
screen.title("Snake game")
screen.tracer(0)
border = Border()
# asking about start
game = True
start_game = screen.textinput(title="Snake Game", prompt="Are you ready? Type 'y' or 'n': ")
if start_game == "n":
    game = False
# set variables
snake = Snake()
food = Food()
score = Scoreboard()
move_keys = Instructions()
move_keys.instructions()

# set moving keys
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

# start the game
while game:
    # update the screen
    screen.update()
    # set moving speed
    time.sleep(SNAKE_SPEED)
    # move
    snake.move()
    # check collision with food and increase the size and score
    if snake.head.distance(food) < 21:
        food.refresh()
        snake.extend()
        score.increase_score()

    # check collision with the wall and reset
    if snake.head.xcor() < -236 or snake.head.xcor() > 236 or snake.head.ycor() < -236 or snake.head.ycor() > 236:
        score.reset()
        snake.reset()

    # check collision with itself and reset
    for x in snake.snakes[1:]:
        if snake.head.distance(x) < 10:
            score.reset()
            snake.reset()
# screen exit on click
screen.exitonclick()
