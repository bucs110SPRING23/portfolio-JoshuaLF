import random
import turtle

# PART A

screen = turtle.Screen()
turt1 = turtle.Turtle()
turt2 = turtle.Turtle()

turt1.shape("turtle")
turt2.shape("turtle")

def home():
    turt1.penup()
    turt2.penup()

    turt1.goto(-100, 20)
    turt2.goto(-100, -20)

    turt1.pendown()
    turt2.pendown()

home()

turt1.speed(1)
turt2.speed(1)

# Race 1

rand1 = random.randint(1, 100)
turt1.forward(rand1)

rand2 = random.randint(1, 100)
turt2.forward(rand2)

home()

# Race 2

home()

for _ in range(50):
    random1 = random.randrange(1, 11)
    random2 = random.randrange(1, 11)

    turt1.forward(random1)
    turt2.forward(random2)

home()

screen.exitonclick()

# PART B

def updateS(time): #creates a function for easier screen updating
    # keep the game looping
    running = True

    # game loop makes sure something is always happening
    while running:

        pygame.event.get()

        if time > 0:
            pygame.time.wait(time)
            running = False

    # for loop through the event queue
        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

import pygame
import math
import random

# initialize pygame
pygame.init()

# set up the window
window = pygame.display.set_mode((500, 500))

# set up colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [red, green, blue]

# set up data
points = []
num_sides = [3, 4, 6, 20, 100, 360]
side_length = 50
xpos = 50
ypos = 50

# draw the shapes
for i in range(len(num_sides)):
    # generate points for the polygon
    for j in range(num_sides[i]):
        angle = 360/num_sides[i]
        radians = math.radians(angle * j)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x, y])

    # draw the polygon
    color = random.choice(colors)
    pygame.draw.polygon(window, color, points)

    # clear the screen and points list
    pygame.display.flip()
    updateS(1000)
    window.fill(black)
    pygame.display.flip()
    points = []