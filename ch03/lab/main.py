#PART A

import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode()
screen_size_variable = pygame.display.get_window_size()
screen_width = screen_size_variable[0]
screen_height = screen_size_variable[1]
screen = pygame.display.set_mode(screen_size_variable)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill((200, 200, 200))

dartboard_center = (screen_width // 2, screen_height // 2)
dartboard_radius = screen_height // 2
pygame.draw.circle(screen, RED, dartboard_center, dartboard_radius)

ring_radius = dartboard_radius
ring_width = 5
pygame.draw.circle(screen, BLACK, dartboard_center, ring_radius, ring_width)

line_width = 5
pygame.draw.line(screen, BLUE, (0, screen_height // 2), (screen_width, screen_height // 2), line_width)
pygame.draw.line(screen, BLUE, (screen_width // 2, 0), (screen_width // 2, screen_height), line_width)

# PART B

for i in range(10):
    x = random.randrange(screen_width)
    y = random.randrange(screen_height)

    distance_from_center = math.hypot(x - dartboard_center[0], y - dartboard_center[1])
    is_in_circle = distance_from_center <= dartboard_radius

    if is_in_circle:
        pygame.draw.circle(screen, GREEN, (x, y), 10)
    else:
        pygame.draw.circle(screen, WHITE, (x, y), 10)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
            running = False
pygame.quit()