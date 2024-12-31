import turtle
from stateLocator import StateLocator
from scoreboard import Scoreboard
from turtle import Screen


# Declare objects
StateLocator = StateLocator()
Scoreboard = Scoreboard()

# Screen declare
screen = Screen()
screen.setup(width=725, height=800)
screen.title("US States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)


quiz_is_on = True

# Start quiz
while quiz_is_on:
    quiz_is_on = StateLocator.user_input()
    if quiz_is_on:
        if StateLocator.input not in StateLocator.already_identified:
            StateLocator.already_identified.append(StateLocator.input)
            Scoreboard.update_score()

# Quiz end game
Scoreboard.end_game()
Scoreboard.update_highscore()
screen.exitonclick()
