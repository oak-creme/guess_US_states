import turtle
import pandas

screen = turtle.Screen()

#create screen, import US map image
us_map = "us_map.gif"
screen.addshape(us_map)
turtle.shape(us_map)

states_locations = pandas.read_csv("50_states.csv")

state_names = states_locations.state
x_cors = states_locations.x
y_cors = states_locations.y

state_list = states_locations["state"].to_list()

state_guess = screen.textinput("guess a state", "what is ur guess?")

if state_guess in state_list:

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = states_locations[states_locations.state == state_guess]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_guess)




screen.exitonclick()
