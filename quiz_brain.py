import pandas
import turtle as t
FONT = ("Arial", 5, "normal")
FILEPATH = "50_states.csv"


class Brain:
    def __init__(self):
        self.pencil = t.Turtle()
        self.pencil.penup()
        self.pencil.hideturtle()
        self.data = pandas.read_csv(FILEPATH)
        self.already_guessed = []

    def check_answer(self, user_answer):
        if len(self.data[self.data.state == user_answer]) > 0 and user_answer not in self.already_guessed:
            state_data = self.data[self.data.state == user_answer]
            position_data = (state_data.x.item(), state_data.y.item())
            self.pencil.goto(position_data)
            self.pencil.write(arg=user_answer, font=FONT)
            self.already_guessed.append(user_answer)

    def user_score(self):
        return len(self.already_guessed)

    def user_gave_up(self):
        not_guessed_states = []
        state_list = self.data["state"].to_list()
        for state in state_list:
            if state not in self.already_guessed:
                not_guessed_states.append(state)
        return not_guessed_states

