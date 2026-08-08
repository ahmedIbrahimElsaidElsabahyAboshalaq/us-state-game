from turtle import Turtle,Screen

import pandas

timmy = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.title("US State Game")
screen.addshape(image)
timmy.shape(image)
guessed_states = []
missing_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)} of 50 are correct" ,
                                    prompt= "What's another state name").title()
    print(answer_state)

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state)
if len(guessed_states) < 50:
    for state in all_states:
        if state not in guessed_states:
            missing_states.append(state)

print(missing_states)
df = pandas.DataFrame(missing_states , columns=["missing_state"])
df.to_csv("missing_states.csv" , index=False)

