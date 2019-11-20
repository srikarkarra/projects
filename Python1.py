import turtle

wn = turtle.Screen()
wn.title("Pong by Srikar")
wn.bgcolor("black")
wn.setup(width = 800,height = 600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
# Padde B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 2.2
ball.dy = 2.2


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    ydown = paddle_a.ycor()
    ydown-=20
    paddle_a.sety(ydown)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    ydown = paddle_b.ycor()
    ydown-=20
    paddle_b.sety(ydown)

# Keyboard Binding
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")

# Main game loop
while True:
    wn.update()
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
