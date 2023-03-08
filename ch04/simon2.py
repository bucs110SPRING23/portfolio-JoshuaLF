import random
import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = screen.get_size()

hitbox_width = width / 2
hitbox_height = height / 2

hitboxes = {
    "red": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "green": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "blue": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "purple": pygame.Rect(0, 0, hitbox_width, hitbox_height)
}

# pygame.Rect - keeps track of x, y coordinates, width, and height
#   - Do NOT track visuals
#   - pygame.Rect(x, y, width, height)
#       - x and y are the top left corner coordinates

hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright

font = pygame.font.SysFont("Arial", 24)

done = False
result = []
turns = 0

order = list(hitboxes.keys())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random.shuffle(order) #shuffles the color order (resets)
                turns = len(order)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turns -= 1
            if hitboxes["red"].collidepoint(event.pos):
                result.append("red")
            elif hitboxes["green"].collidepoint(event.pos):
                result.append("green")
            elif hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
            elif hitboxes["purple"].collidepoint(event.pos):
                result.append("purple")
            
    if turns == 0:
        if result == order:
            font.render("You win!", True, "white")
        else:
            font.render("You lose.", True, "white")
    
    screen.fill(0, 0, 0)

    for c, hb in hitboxes.items():
        box = pygame.draw.rect(screen, c, hb)
        screen.blit(box, hb)