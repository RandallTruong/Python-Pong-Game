# Pong Game

# Turtle module lets you do basic graphics and is good for starting with games
import turtle

# Creating a window
window = turtle.Screen()
window.title("Pong Game by Randall Truong")
# Setting background color for window
window.bgcolor("Blue")
# Setting size of window
window.setup(width=800, height=600)
# Tracer stops the window from updating so it speeds up the game
window.tracer(0)

# Score
Score_1 = 0
Score_2 = 0

# Paddle one
# turtle is the module name and Turtle is the class name
paddle_one = turtle.Turtle()
# Set animation speed to the maximum possible speed
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("orange")
# Stretch the width by 5 and keep the length the same
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
# penup because we do not want to draw a line when paddle moves
paddle_one.penup()
# Where the paddle starts (coordinates)
paddle_one.goto(-350, 0)

# Paddle Two
# turtle is the module name and Turtle is the class name
paddle_two = turtle.Turtle()
# Set animation speed to the maximum possible speed
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("orange")
# Stretch the width by 5 and keep the length the same
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
# Where the paddle starts (coordinates)
paddle_two.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
# penup because we do not want to draw a line when ball moves
ball.penup()
ball.goto(0, 0)
# Split the ball's movement to an x movement and a y movement
# dx means change in x & dy means change in y
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# Hide the pen
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2:0", align="center",
          font=("Courier", 24, "normal"))

# Function
def paddle_one_up():
    y_coordinate = paddle_one.ycor()  # Sets the current y coordinate to the variable
    y_coordinate += 50  # Add 50 pixels to the y coordinate
    paddle_one.sety(y_coordinate)  # Sets the new y coordinate

def paddle_one_down():
    y_coordinate = paddle_one.ycor()  # Sets the current y coordinate to the variable
    y_coordinate -= 50  # Removes 50 pixels from the y coordinate
    paddle_one.sety(y_coordinate)  # Sets the new y coordinate

def paddle_two_up():
    y_coordinate2 = paddle_two.ycor()
    y_coordinate2 += 50
    paddle_two.sety(y_coordinate2)

def paddle_two_down():
    y_coordinate2 = paddle_two.ycor()
    y_coordinate2 -= 50
    paddle_two.sety(y_coordinate2)

# Keyboard Binding
window.listen()  # This tells the window to listen for keyboard input
# When user presses w call the function paddle_one_up
window.onkeypress(paddle_one_up, "w")

window.listen()  # This tells the window to listen for keyboard input
# When user presses s call the function paddle_one_down
window.onkeypress(paddle_one_down, "s")

window.listen()
# When user presses up arrow call the function paddle_two_up
window.onkeypress(paddle_two_up, "Up")

window.listen()
# When user presses down arrow call the function paddle_two_down
window.onkeypress(paddle_two_down, "Down")

# Main game loop
while True:
    window.update()  # Everytime the loop runs it updates the screen
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # (Top Border)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverses direction

    # (Bottom Border)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverses direction

    # (Right Border)
    if ball.xcor() > 390:
        ball.goto(0, 0)  # Ball goes back to center
        ball.dx *= -1
        Score_1 += 1  # Increase player 1 score by 1
        pen.clear() #Removes old score
        pen.write("Player 1: {} Player 2: {}".format(Score_1, Score_2), align="center",
                  font=("Courier", 24, "normal")) #Updates Score

    # (Left Border)
    if ball.xcor() < -390:
        ball.goto(0, 0)  # Ball goes back to center
        ball.dx *= -1
        Score_2 += 1  # Increase player 2 score by 1
        pen.clear() #Removes old score
        pen.write("Player 1: {} Player 2: {}".format(Score_1, Score_2), align="center",
                  font=("Courier", 24, "normal")) #Updates Score

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_two.ycor() + 60 and ball.ycor() > paddle_two.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1  # Reverse direction of ball

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_one.ycor() + 60 and ball.ycor() > paddle_one.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1  # Reverse direction of ball
