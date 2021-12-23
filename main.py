from turtle import Screen, Turtle

# create the screen for the Pong game
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# When you turn off the animation you need to manually
#Update the screen and refresh it every single time
#using while loop
screen.tracer(0)

# adding the paddle to the game
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


# set up the paddle listner
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True

while game_is_on:
    screen.update() # show every thing which happened so far




screen.exitonclick()

