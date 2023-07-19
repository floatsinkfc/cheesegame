import os
import turtle
import time

gb = turtle.Screen()
gb.title("Cheese Game")
gb.bgcolor("lightgreen")
gb.tracer(3)

# Global variables to track the current screen state
is_instructions_screen = False

def press_start(x, y):
    gb.clear()  # Clear the screen
    os.system('python cheesegame.py')
    os._exit(0)

def press_instructions(x, y):
    global is_instructions_screen
    is_instructions_screen = True
    gb.clear()  # Clear the screen
    gb.bgcolor("lightgreen")
    # Display instructions
    instructions_text = "Instructions:\n\nYour goal is to collect cheese while avoiding red and black cheese.\n\nUse the W-A-S-D keys to move the player.\n\nPress Spacebar to activate a speed boost.\n\nCollect as much cheese as you can before reaching 100 points!\n\nGood luck!"
    instructions = turtle.Turtle()
    instructions.color("black")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, 0)
    instructions.write(instructions_text, align="center", font=("Arial", 20, "normal"))

    # Click to Continue Text
    contbutton = turtle.Turtle()
    contbutton.color("black")
    contbutton.penup()
    contbutton.goto(0, -250)
    contbutton.write("Click to Continue", align="center", font=("Arial", 20, "normal"))
    contbutton.shape('square')
    contbutton.shapesize(4,12)  # Increase the size of the clickable area
    contbutton.onclick(press_continue)

def press_continue(x, y):
    global is_instructions_screen
    if is_instructions_screen:
        is_instructions_screen = False
        gb.clear()  # Clear the screen
        gb.bgcolor("lightgreen")
        draw_buttons()
        turtle.onscreenclick(on_click)  # Re-register the main button clicks

def draw_buttons():
    # Title Text
    current_time = time.ctime()
    title_text = "Cheese Game"
    title = turtle.Turtle()
    title.color("black")
    title.penup()
    title.goto(0, 200)
    title.write("         " + title_text + "\n" + current_time, align="center", font=("Arial", 40, "bold"))
    title.hideturtle()

    # Start Text
    start_text = turtle.Turtle()
    start_text.color("black")
    start_text.penup()
    start_text.goto(0, -100)
    start_text.write("Start", align="center", font=("Arial", 20, "normal"))
    start_text.shape('square')
    start_text.shapesize(4,12)  # Increase the size of the clickable area
    start_text.hideturtle()
    start_text.onclick(press_start)

    # Instructions Text
    instructions_text = turtle.Turtle()
    instructions_text.color("black")
    instructions_text.penup()
    instructions_text.goto(0, -200)
    instructions_text.write("Instructions", align="center", font=("Arial", 20, "normal"))
    instructions_text.shape('square')
    instructions_text.shapesize(4,12)  # Increase the size of the clickable area
    instructions_text.hideturtle()
    instructions_text.onclick(press_instructions)

def on_click(x, y):
    global is_instructions_screen
    if is_instructions_screen:
        press_continue(x, y)
    else:
        if -150 < x < 150 and -130 < y < -70:
            press_start(x, y)
        elif -150 < x < 150 and -230 < y < -170:
            press_instructions(x, y)

draw_buttons()
turtle.onscreenclick(on_click)

turtle.listen()
turtle.mainloop()
