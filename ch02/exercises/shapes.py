import pygame

pygame.init()

screen = pygame.display.set_mode()

screen.fill("white")

dimensions = screen.get_size() # [width, and height]

#dividing dimension by 2 for middle point
starting_point = list((dimensions[0] // 2, dimensions[1] // 2 + 100))

radius = 200

for _ in range(3):
    pygame.draw.circle(screen, "black", starting_point, radius, 3)
    starting_point[1] = starting_point[1] - radius
    radius = radius // 2
    starting_point[1] = starting_point[1] - radius + radius // 10

pygame.display.flip() #actually draws it on the screen

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
