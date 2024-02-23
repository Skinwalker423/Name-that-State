from turtle import Turtle, Screen
import pandas
import time
from map import Map
from state import State

screen = Screen()
screen.title("The U.S. States Game")
screen.addshape("blank_states_img.gif")
new_map = Map()

states_csv = pandas.read_csv("50_states.csv")


# state = Turtle()
# state.color("red")
# state.goto(-297, 13)


def find_state(user_input):
    state_found = states_csv[states_csv.state == user_input]
    if state_found["x"].any() and state_found["y"].any():
        x = state_found["x"].item()
        y = state_found["y"].item()

        new_state = State()
        new_state.goto(x, y)
        new_state.clear()
        new_state.write(arg=user_input)
        return True
    else:
        print("State not found. You lose")
        return False


is_game_on = True
score = 0
answer_list = []

while is_game_on and score < 50:
    screen.update()
    time.sleep(1)
    user_answer = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state name?").title()
    if user_answer == "Exit" or not user_answer:
        is_game_on = False
    elif user_answer in answer_list:
        print("You already got that state. Try again")
    else:
        if find_state(user_answer):
            score += 1
            answer_list.append(user_answer)
        else:
            is_game_on = False
            print(f"final score: {score}")

# states_not_in_list = states_csv[~states_csv.isin(answer_list)].dropna()
missed_states = [state for state in states_csv["state"] if state not in answer_list]
print(missed_states)
states_not_in_list = pandas.DataFrame(missed_states)
states_not_in_list.to_csv("missed_states.csv")

screen.exitonclick()
