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
GREEN = (0, 170, 0)
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

# PART A

font = pygame.font.Font(None, 48)

player1_color = GREEN
player2_color = BLUE
player1_score = 0
player2_score = 0

for round_num in range(1, 21):
    if round_num % 2 == 1:
        player_name = "Player 1"
        player_color = player1_color
    else:
        player_name = "Player 2"
        player_color = player2_color

    x = random.randrange(screen_width)
    y = random.randrange(screen_height)

    distance_from_center = math.hypot(x - dartboard_center[0], y - dartboard_center[1])
    is_in_circle = distance_from_center <= dartboard_radius

    if is_in_circle:
        score = 1
        pygame.draw.circle(screen, player_color, (x, y), 10)
    else:
        score = 0
        pygame.draw.circle(screen, WHITE, (x, y), 10)

    if round_num % 2 == 1:
        player1_score += score
    else:
        player2_score += score

    text = font.render(f"{player_name} throws...{'hit' if is_in_circle else 'miss'}", True, player_color)
    screen.blit(text, (20, 20 + (round_num - 1) * 30))
    pygame.display.flip()
    pygame.time.wait(1000)

text = font.render("Game over", True, BLACK)
screen.blit(text, (20, 20 + 20 * 30))
text = font.render(f"Player 1 score: {player1_score}", True, player1_color)
screen.blit(text, (20, 20 + 21 * 30))
text = font.render(f"Player 2 score: {player2_score}", True, player2_color)
screen.blit(text, (20, 20 + 22 * 30))

if player1_score > player2_score:
    winner = "Player 1 wins!"
    winner_color = player1_color
elif player2_score > player1_score:
    winner = "Player 2 wins!"
    winner_color = player2_color
else:
    winner = "It's a tie!"
    winner_color = BLACK

text = font.render(winner, True, winner_color)
screen.blit(text, (20, 20 + 23 * 30))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
            running = False
pygame.quit()