import pygame
import point

def mainloop(display):
    points = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_deleted = False
                for i, p in enumerate(points):
                    if p.rect.collidepoint(event.pos): #gets position of mouse click
                        del points[i]
                        point_deleted = True
                if not point_deleted:
                    p = point.Point(event.pos[0], event.pos[1])
                    # little trick: (*event.pos) (treats like two parameters)
                    points.append(p)

        display.fill("white")

        for p in points:
            pygame.draw.circle(display, p.color, p.rect.center, p.rect.h / 2)

        pygame.display.flip()

def main():
            pygame.init()
            display = pygame.display.set_mode()
            mainloop(display)

main()