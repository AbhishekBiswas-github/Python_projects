from turtle import Turtle

# CONSTANTS
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_MOVEMENT = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

SNAKE_COLOR = 'white'
SNAKE_SHAPE = 'square'


# Snake Class
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    # Create snake
    def create_snake(self):
        for pos in SNAKE_POSITIONS:
            self.add_parts(pos)

    # Add parts
    def add_parts(self,pos):
        snake_part = Turtle()
        snake_part.color(SNAKE_COLOR)
        snake_part.shape(SNAKE_SHAPE)
        snake_part.penup()
        snake_part.goto(pos)
        self.snake_body.append(snake_part)

    # Extend Snake
    def extend_snake(self):
        self.add_parts(self.snake_body[-1].position())

    # Move snake
    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.head.forward(SNAKE_MOVEMENT)

    # Move snake using key stokes
    def up(self):
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    # X and Y cods of shake head
    def snake_x_cor(self):
        return abs(int(self.head.xcor()))

    def snake_y_cor(self):
        return abs(int(self.head.ycor()))

