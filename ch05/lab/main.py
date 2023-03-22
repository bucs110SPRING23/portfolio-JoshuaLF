import pygame

def main():
    result = threenp1range(int(input("What is the upper limit?")))

    graph_coordinates(result)

# PART A

def threenp1(n):
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count += 1
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1):
        num = threenp1(i)
        objs_in_sequence[i] = num
    return objs_in_sequence

# PART B

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    coords = []
    for x, y in threenplus1_iters_dict.items():
        coords.append((x, y))

    scaled_coordinates = []
    for x, y in coords:
        scaled_x = x * 5
        scaled_y = screen_height - y * 5
        scaled_coordinates.append((scaled_x, scaled_y))
    
    if len(scaled_coordinates) >= 2:
        pygame.draw.lines(screen, "white", False, scaled_coordinates)

    flipped_screen = pygame.transform.flip(screen, False, True)
    flipped_width, flipped_height = flipped_screen.get_size()
    flipped_screen = pygame.transform.scale(flipped_screen, (flipped_width * 5, flipped_height * 5))

    max_so_far = 0
    maxVal = 0
    for n, iters in threenplus1_iters_dict.items():
        if iters > max_so_far:
            max_so_far = iters
            maxVal = n

    font = pygame.font.Font(None, 30)
    msg = font.render("Max iterations: "+ str(max_so_far)+" at "+ str(maxVal), True, "white")
    flipped_screen.blit(msg, (10, 10))

    screen.blit(flipped_screen, (0, 0))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

main()