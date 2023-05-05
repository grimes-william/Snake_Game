from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

GAME_SPEED = 0.08


# Screen initialization
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Make the starting snake
snake = Snake()

# Make the food
food = Food()

# Create scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_over = False
while not game_over:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # Food collision detection
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add_score()
        snake.add_square()

    # Wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_over = True
        scoreboard.game_over()

    # Body collision
    for sq in snake.snake_body[1:]:
        if snake.head.distance(sq) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
