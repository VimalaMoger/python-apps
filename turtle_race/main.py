import random
from turtle import Turtle, Screen
import colorname

turtles = []
is_race_on = False
colors = []

def random_color():
    for _ in range(25):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(colorname.get_color_name(r, g, b))

def make_turtle_move():
    global is_race_on
    global colors
    y_position = [-70, -40, -10, 20, 50, 80]
    # We need 6 turtles starting from the same line
    for i in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-350, y=y_position[i])
        turtles.append(new_turtle)

def start_turtle_race(user_input):
    global is_race_on
    if user_input:
        is_race_on = True
    while is_race_on:
        for tr in turtles:
            if tr.xcor() > 330:
                winning_color = tr.pencolor()
                if winning_color == user_input:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You loose! The {winning_color} turtle is the winner!")
                is_race_on = False
            rand_distance = random.randint(0, 10)
            #turtle.dot(5, random.choice(colors))
            tr.forward(rand_distance)

if __name__ == '__main__':
    screen = Screen()
    screen.colormode(255)
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    random_color()
    colors = list(set(colors))
    print(colors[:6])
    user_bet = screen.textinput(f"{colors}", "Which turtle will win the race? Enter a color: ")
    make_turtle_move()
    start_turtle_race(user_bet)
    screen.exitonclick()

