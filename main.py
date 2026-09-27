import turtle
import pandas

screen = turtle.Screen()

#create screen, import US map image
us_map = "us_map.gif"
screen.addshape(us_map)
turtle.shape(us_map)

#return coords of selected US state
def get_mouse_click_coor(x, y):
    print(x, y)

screen.onscreenclick(get_mouse_click_coor)

turtle.mainloop()


screen.exitonclick()