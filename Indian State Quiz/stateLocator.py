import json
from turtle import Turtle, Screen
import pandas as pd


class StateLocator(Turtle):
    def __init__(self):
        super().__init__()
        self.input = ""
        self.details = {
            "states": [],
            "x_cod": [],
            "y_cod": []
        }
        self.state_index = -1
        self.already_identified = []
        self.setStateDetails()

    def setStateDetails(self):
        indian_states = pd.read_csv("Indian_states.csv").to_dict()
        self.details["states"] = list(indian_states["States"].values())
        self.details["x_cod"] = list(indian_states["x"].values())
        self.details["y_cod"] = list(indian_states["y"].values())
        print(json.dumps(self.details, indent=4))

    def user_input(self):
        self.input = Screen().textinput(title="Guess the state", prompt="Enter the state name").title()
        return self.findState()

    def findState(self):
        if self.input in self.details["states"]:
            if self.input not in self.already_identified:
                self.state_index = self.details["states"].index(self.input)
                self.mark_State()
            return True
        else:
            return False

    def mark_State(self):
        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(self.details["x_cod"][self.state_index], self.details['y_cod'][self.state_index])
        state.write(self.input, font=("Arial", 10, "bold"))
