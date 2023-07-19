# Cheese Game By Zi 
# Inspired By TokyoEdtech on YouTube
# https://www.youtube.com/watch?v=PTgyzZGknvg&list=PLlEgNdBJEO-n8FdWb-7f_C4dFC07IY9tb&pp=iAQB

# Importing Turtle
import time
import random
import math
import turtle
import os

# Set Up Background Screen
gb = turtle.Screen()
gb.title("Cheese Game")
gb.bgcolor("lightgreen")
gb.tracer(0)
screen = turtle.Screen()
screen.addshape('mouse.gif')
screen.addshape('cheese.gif')
screen.addshape('cheese2.gif')
screen.addshape('cheese3.gif')
screen.addshape('mouse2.gif')

# Border Draw
border = turtle.Turtle()
border.color("black")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

# Set Up Player Info
player = turtle.Turtle()
player.color("yellow")
player.shape("mouse.gif")
player.penup()
player.speed(0)

# Multiple Score
maxScore = 6
scores = []

for count in range(maxScore):
    scores.append(turtle.Turtle())
    scores[count].color("red")
    scores[count].shape("cheese.gif")
    scores[count].penup()
    scores[count].speed(0)
    scores[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

badScore = turtle.Turtle()
badScore.color("Red")
badScore.shape("cheese2.gif")
badScore.penup()
badScore.speed(0)
badScore.hideturtle()

bomb = turtle.Turtle()
bomb.color("Red")
bomb.shape("cheese3.gif")
bomb.penup()
bomb.speed(0)
bomb.hideturtle()

# Set Up Player Stats
speed = 0.5
playerScore = 0
playerLives = 3
start_time = time.time()
boost_active = False

# Define Function

def turnleft():
    player.setheading(180)
    player.forward(speed)
    player.shape('mouse2.gif')


def turnright():
    player.setheading(0)
    player.forward(speed)
    player.shape('mouse.gif')


def turnup():
    player.setheading(90)
    player.forward(speed)


def turndown():
    player.setheading(270)
    player.forward(speed)

def speedup():
    global speed, boost_active
    if not boost_active:
        speed += 0.2
        boost_active = True
        turtle.ontimer(end_speed_boost, 3000)  # 3 seconds

def end_speed_boost():
    global speed, boost_active
    speed -= 0.2
    boost_active = False


def isCollision(t1, t2):
    if t2.isvisible():
        dis = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if dis < 50:
            return True
    return False

def generate_badScore():
    if not badScore.isvisible():
        badScore.setposition(random.randint(-280, 280), random.randint(-280, 280))
        badScore.right(random.randint(0, 360))
        badScore.showturtle()

def generate_bomb():
    if not bomb.isvisible():
        bomb.setposition(random.randint(-280, 280), random.randint(-280, 280))
        bomb.right(random.randint(0, 360))
        bomb.showturtle()

def hide_badScore():
    badScore.hideturtle()
    turtle.ontimer(generate_badScore, random.randint(5000, 10000))

def hide_bomb():
    bomb.hideturtle()
    turtle.ontimer(generate_bomb, random.randint(5000, 10000))

def updateScore():
    border.undo()
    border.penup()
    border.hideturtle()
    border.setposition(-290, 310)
    border.color("black")
    elapsed_time = int(time.time() - start_time)
    time_string = "              Time: {:02d}:{:02d}".format(elapsed_time // 60, elapsed_time % 60)
    scoreString = "Cheese Earned: %s" % playerScore
    scoreString2 = "            Player Lives: %s" % playerLives
    border.write(scoreString + scoreString2 + time_string, False, align="left",
                 font=("Arial", 14, "normal"))
def check_border(turtle):
    if turtle.xcor() >= 290:
        turtle.setx(290)
        turtle.setheading(random.randint(0, 180))
    elif turtle.xcor() <= -290:
        turtle.setx(-290)
        turtle.setheading(random.randint(0, 180))

    if turtle.ycor() >= 290:
        turtle.sety(290)
        turtle.setheading(random.randint(90, 270))
    elif turtle.ycor() <= -290:
        turtle.sety(-290)
        turtle.setheading(random.randint(90, 270))

# Keyboard Binding
turtle.listen()
turtle.onkey(turnleft, "a")
turtle.onkey(turnright, "d")
turtle.onkey(turnup, "w")
turtle.onkey(turndown, "s")
turtle.onkey(speedup, "space")

# Game Function
while True:
    player.forward(speed)

    # Border
    check_border(player)

    # Update score and timer
    updateScore()

    # Score Move
    for count in range(maxScore):
        scores[count].forward(0.2)

        # Border
        check_border(scores[count])
        check_border(badScore)
        check_border(bomb)

        # Collision
        if isCollision(player, scores[count]):
            if scores[count].isvisible():
                scores[count].setposition(
                    random.randint(-300, 300), random.randint(-300, 300))
                scores[count].right(random.randint(0, 360))
                playerScore += 1

        if isCollision(player, badScore):
            if badScore.isvisible():
                if playerScore > 4:
                    playerScore -= 5
                    badScore.hideturtle()
                    badScore.setposition(400, 400)
                else:
                    playerScore -= playerScore
                    badScore.hideturtle()
                    badScore.setposition(400, 400)

        if isCollision(player, bomb):
            if bomb.isvisible():
                playerLives -= 1
                bomb.hideturtle()
                bomb.setposition(400, 400)

        if playerScore >= 0:
            badScore.forward(0.05)
            bomb.forward(0.05)

        if playerScore > 0 and not badScore.isvisible() and not playerScore >= 100 and playerLives > 0:
            generate_badScore()

        if playerScore > 0 and not bomb.isvisible() and not playerScore >= 100 and playerLives > 0:
            generate_bomb()

        if playerScore == 100 and player.isvisible():
            elapsed_time = int(time.time() - start_time)
            os.system(f'python gameend.py {playerScore} {playerLives} {elapsed_time}')
            os._exit(0)

        if playerLives <= 0:
            elapsed_time = int(time.time() - start_time)
            os.system(f'python gameend.py {playerScore} {playerLives} {elapsed_time}')
            os._exit(0)

    turtle.update()

delay = input("Press Enter to Finish: ")
