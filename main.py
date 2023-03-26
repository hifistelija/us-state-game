import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the data from CSV file
states_data = pd.read_csv("50_states.csv")


def display_state(state_name, x, y):
    state_writer = turtle.Turtle()
    state_writer.hideturtle()
    state_writer.penup()
    state_writer.goto(x, y)
    state_writer.write(state_name, align="center", font=("Arial", 12, "normal"))


# Keep track of the guessed states
guessed_states = []

while len(guessed_states) < 50:
    # prompt user and capture answer
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's a another state's name?").title()

    # Exit game
    if answer_state == "Exit":
        break

    # Check if the answer is in the list of states
    if answer_state in states_data.state.values and answer_state not in guessed_states:
        # Get the coordinates of the state
        state_row = states_data[states_data.state == answer_state]
        x = int(state_row.x)
        y = int(state_row.y)

        # Display state name on the map
        display_state(answer_state, x, y)

        # Add the state to the list of guessed states
        guessed_states.append(answer_state)

# print the states that were not guessed
missed_states = [state for state in states_data.state if state not in guessed_states]
missed_states_data = states_data[states_data["state"].isin(missed_states)]
missed_states_data.to_csv("missed_states_data.csv")

# Close the turtle window
turtle.mainloop()
