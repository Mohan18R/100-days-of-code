import turtle

# Create the screen
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off the screen updates

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Paddle movement functions
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(paddle_right, "Right")
wn.onkey(paddle_left, "Left")

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -240)
ball.dx = 0.2
ball.dy = 0.2

# Bricks
bricks = []

# Create bricks
for i in range(5):
    for j in range(7):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("blue")
        brick.shapesize(stretch_wid=1, stretch_len=4)  # Rectangle shape
        brick.penup()
        brick.goto(-290 + j * 90, 250 - i * 30)
        bricks.append(brick)

# Score
score = 0

# Scoreboard
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Update the score display
def update_score():
    global score
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Game over display
game_over_display = turtle.Turtle()
game_over_display.speed(0)
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()

def game_over():
    game_over_display.goto(0, 0)
    game_over_display.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
    wn.update()

# Main game loop
game_is_on = True
while game_is_on:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border collision
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        game_is_on = False  # End the game loop
        game_over()
    
    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-230)
        ball.dy *= -1
    
    # Brick collision
    for brick in bricks:
        if brick.isvisible() and (brick.distance(ball) < 50):  # Adjusted for rectangle
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            score += 10  # Increase score
            update_score()
            break

# Hold the window open
turtle.done()
