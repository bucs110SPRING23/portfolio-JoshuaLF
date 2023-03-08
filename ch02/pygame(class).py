import pygame

pygame.init()

# gets the display and makes it full screen
# no arguments means full screen
screen = pygame.display.set_mode()

screen.fill("red")
pygame.display.flip()
pygame.time.wait(5000)

screen.fill("green")
pygame.display.flip()
pygame.time.wait(500)

screen.fill("blue")
pygame.display.flip()

screen_size = screen.get_size()

# [x, y, width, height]
dimensions = [100, 200, 250, 150]
pygame.draw.rect(screen, "red", dimensions)

dimensions = [300, 300, 250, 150]
pygame.draw.rect(screen, "yellow", dimensions)

pygame.display.flip()

# keep the game looping
running = True

# game loop
while running:

   pygame.event.get()

# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False