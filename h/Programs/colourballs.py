import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

# Create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)

# Ball movement variables
ball.dx = random.choice([-3, 3])
ball.dy = random.choice([-3, 3])

# Game loop
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Bounce on walls
    if ball.xcor() > 200 or ball.xcor() < -200:
        ball.dx *= -1
        ball.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))

    if ball.ycor() > 200 or ball.ycor() < -200:
        ball.dy *= -1
        ball.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))

    screen.update()
