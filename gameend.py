import turtle
import sys
import os

# Get player score and lives from command-line arguments
playerScore = int(sys.argv[1]) if len(sys.argv) > 1 else 0
playerLives = int(sys.argv[2]) if len(sys.argv) > 2 else 0
elapsedTime = int(sys.argv[3]) if len(sys.argv) > 3 else 0

# Set up the turtle screen
gb = turtle.Screen()
gb.title("Game End")
gb.bgcolor("lightgreen")
gb.tracer(0)

# Function to start the game again
def start_game():
    gb.bye()  # Close the turtle screen
    # Call the cheesegame.py script
    os.system('python cheesegame.py')

if playerLives == 0:
    title_text = "Game Over! You Lost!"
if playerScore == 100:
    title_text = "Very Cheesy! You Won!!"

def title_change():
    title = turtle.Turtle()
    title.color("black")
    title.penup()
    title.goto(0, 200)
    title.write("" + title_text, align="center", font=("Arial", 40, "bold"))
    title.hideturtle()

# Display player score and lives
title_change()
score_text = "Score: {}".format(playerScore)
lives_text = "Lives: {}".format(playerLives)
time_text = "Time: {:02d}:{:02d}".format(elapsedTime // 60, elapsedTime % 60)
score_display = turtle.Turtle()
score_display.color("black")
score_display.penup()
score_display.goto(0, 0)
score_display.write(score_text + "\n" + lives_text + "\n" + time_text, align="center", font=("Arial", 20, "normal"))
score_display.hideturtle()

# Display start again text
start_again_text = turtle.Turtle()
start_again_text.color("black")
start_again_text.penup()
start_again_text.goto(0, -100)
start_again_text.write("Click to Start Again", align="center", font=("Arial", 20, "normal"))

# Function to handle the click event
def handle_click(x, y):
    start_game()

# Register the click event
turtle.onscreenclick(handle_click)

turtle.mainloop()
