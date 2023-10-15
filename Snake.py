import turtle
import time

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90.0
DOWN = 270.0
LEFT = 180.0
RIGHT = 0.0


class Snakes:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add_snake(position)

    def add_snake(self, pos):
        snake = turtle.Turtle('square')
        snake.color('VioletRed1')
        snake.penup()
        snake.goto(pos)
        self.snake_parts.append(snake)

    def extend_snake(self):
        print(self.snake_parts[-1].position())
        self.add_snake(self.snake_parts[-1].position())

    def move(self):
        time.sleep(0.3)
        for part_index in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_index - 1].xcor()
            new_y = self.snake_parts[part_index - 1].ycor()
            self.snake_parts[part_index].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for part in self.snake_parts:
            part.goto(100, 1000)
        self.snake_parts.clear()
        self.create_snake()

    def up(self):
        # print(self.snake_parts[0].heading())
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def down(self):
        # print(self.snake_parts[0].heading())
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    def left(self):
        # print(self.snake_parts[0].heading())
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)

    def right(self):
        # print(self.snake_parts[0].heading())
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)
