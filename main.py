import turtle
import pandas

screen = turtle.Screen()

#create screen, import US map image
us_map = "us_map.gif"
screen.addshape(us_map)
turtle.shape(us_map)

states_locations = pandas.read_csv("50_states.csv")

#coordinates of all states
state_names = states_locations.state
x_cors = states_locations.x
y_cors = states_locations.y

#list of all the states
state_list = states_locations["state"].to_list()

#list of previously guessed states
guessed_states = []

#while the user has not guessed all 50 states, they can continue to guess
while len(guessed_states) < 50:

    #user guess
    state_guess = screen.textinput(f"{len(guessed_states)}/50 states correct",
                                   "guess a state").title()

    #text box
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    #user can exit early
    if state_guess == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states = pandas.DataFrame(missing_states)
        missing_states.to_csv("missing_states.csv")
        break

    #if answer is correct, print the state name and add it to 'guessed_states'
    if state_guess in state_list:

        guessed_states.append(state_guess)
        state_data = states_locations[states_locations.state == state_guess]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_guess)

    #if user guesses all 50 states, they win
    if len(guessed_states) == 50:
        t.goto(0, 0)
        t.write("YOU WIN!", False, "center", ("Arial", 18, "bold"))

