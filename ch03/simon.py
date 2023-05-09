# Simon Says

import pygame
import random

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

pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    #pygame.time.wait(1000)
    updateS(1000)

    screen.fill("black")
    pygame.display.flip()
    #pygame.time.wait(250)
    updateS(250)

message = """
    Simon says:
    UP: RED
    DOWN: BLUE
    LEFT: GREEN 
    RIGHT: YELLOW

    click on the window, enter sequence, m then press enter
"""

response = input(message)

user_sequence = []
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("UP")
            user_sequence.append("red")
        elif event.key == pygame.K_DOWN:
            print("DOWN")
            user_sequence.append("blue")
        elif event.key == pygame.K_LEFT:
            print("LEFT")
            user_sequence.append("green")
        elif event.key == pygame.K_RIGHT:
            print("RIGHT")
            user_sequence.append("yellow")

print("")
print("User sequence:", user_sequence)

if user_sequence == colors:
    print("You win!")
else:
    print("Were you even paying attention?")