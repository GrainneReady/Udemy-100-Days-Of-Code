# This is a program I made following Udemy's Day 25 of 100 Days of Code (Instructor-Led Course)
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
import turtle
import pandas
BLANK_US_IMAGE = "Days\\Day 25\\Project - US States Game\\blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(BLANK_US_IMAGE)
turtle.shape(BLANK_US_IMAGE)


# def get_mouse_click_coor(x, y): - Get coordinates of mouse click, useful for plotting
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

# Challenge:
#   1. Convert the guess to Title case ✔
#   2. Check if the guess is among the 50 states ✔
#   3. Write correct guesses onto the map ✔
#   4. Use a loop to allow the user to keep guessing ✔
#   5. Record the correct guesses in a list ✔
#   6. Keep track of the score ✔


def add_state_to_map(state_name):
    """Adds a state to the map displayed on screen, with its name at its respective x, y coordinates by making a Turtle object
    Will also add the state name to the list of correct guesses

    Args:
        state_name (String): The name of the state to add
    """
    stateToAdd = states_data[states_data.state == answer_state]
    correct_guesses.append(answer_state)
    new_state = turtle.Turtle(visible=False)
    new_state.penup()
    new_state.goto(int(stateToAdd.x.values), int(stateToAdd.y.values))
    # new_state.write(stateToAdd.state.item())    # get raw value of state
    new_state.write(answer_state, align="CENTER")   # Or just get answer state as its also the raw value, but formatted and titlecased


def missed_states(correct_guesses, states_names):
    """Compares the states correctly guessed in a list (correct_guesses) to the total list of state names in the US (state_names)
    Will create a csv of all the states that were in states_names but were not in correct_guesses

    Args:
        correct_guesses (list): The names of states in the United States that the user guessed correctly
        states_names (list): The full list of states in the United States
    """
    missing_states = [state for state in state_names if state not in correct_guesses]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv(("Days\\Day 26\\Project - US States Game (Updated)\\states_to_learn.csv"))


states_data = pandas.read_csv("Days\\Day 26\\Project - US States Game (Updated)\\50_states.csv")
correct_guesses = []
state_names = states_data.state.values
answer_state = ""
while len(correct_guesses) < 50 and answer_state != "Exit":
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in state_names and answer_state not in correct_guesses:  # If the guessed state is a state from 50_states.csv and was not guessed previously
        add_state_to_map(answer_state)
missed_states(correct_guesses=correct_guesses, states_names=state_names)
