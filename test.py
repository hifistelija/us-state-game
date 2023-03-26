import pandas as pd

states_data = pd.read_csv("50_states.csv")

# print(states_data.columns)
print(states_data.state.values)  # prints list of states

state_row = states_data[states_data.state == "Ohio"]
print(state_row)
print(state_row.x)
print(states_data[states_data.state == "Ohio"].x)
print(states_data)
print(states_data.state)

# use states_data.state.values to check membership in state data or convert state column data to a list "_
