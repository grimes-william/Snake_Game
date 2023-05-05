from turtle import Turtle
X_COR = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[len(self.snake_body) - 1]

    # Create the snake with 3 squares
    def create_snake(self):
        for _ in range(0, 3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(X_COR[_], 0)

            self.snake_body.append(new_square)

    # Move loop
    def move(self):
        for sq in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[sq - 1].xcor()
            y_cor = self.snake_body[sq - 1].ycor()
            self.snake_body[sq].goto(x_cor, y_cor)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # Adding body segment when food is eaten
    def add_square(self):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(self.tail.xcor(), self.tail.ycor())

        self.snake_body.append(new_square)
