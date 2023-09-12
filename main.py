import pandas

from quiz_brain import Brain
import turtle as t


screen = t.Screen()
screen.title("U.S. Quiz Game")
image = "blank_states_img.gif"
screen.setup(width=800, height=600)
screen.addshape(image)
t.shape(image)
brain = Brain()

while brain.user_score() < 50:
    answer_state = screen.textinput(title=f"Guess the state [{brain.user_score()}/50]", prompt="Type a "
                                                                                               "state's name").title()
    if answer_state == "Exit":
        break
    else:
        brain.check_answer(answer_state)

not_guessed_states = {
    "state": brain.user_gave_up()
}
pandas.DataFrame(not_guessed_states).to_csv("not_guessed_states.csv")
