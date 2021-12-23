from turtle import Screen, Turtle
from paddle import Paddle



# create the screen for the Pong game
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# When you turn off the animation you need to manually
#Update the screen and refresh it every single time
#using while loop
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))




# set up the paddle listner
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




game_is_on = True

while game_is_on:
    screen.update() # show every thing which happened so far




screen.exitonclick()

