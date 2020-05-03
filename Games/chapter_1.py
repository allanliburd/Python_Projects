import pygame

pygame.init()

window = pygame.display.set_mode((500,400))

while True:
    # Rectangle (red, gree, blue), position
    pygame.draw.rect(window, (255, 0, 0), (100, 1000, 50, 30))
    pygame.draw.rect(window, (0, 255, 0), (150, 100, 50, 30))
    pygame.draw.rect(window, (0, 0, 255), (200, 100, 50, 30))
    # Circle (red, green, blue), (x coord, y coord), radius, height, width
    pygame.draw.circle(window, (255, 0, 0), (250, 200), 20, 0)
    pygame.draw.circle(window, (0, 255, 255), (150, 100), 25, 5)
    # Ellipse (red, green, blue), (x coord, y coord), radius, height, width
    pygame.draw.ellipse(window, (255, 0, 255), (250, 200, 50, 40))
    # Line (single)
    pygame.draw.line(window, (255, 0, 0), (100, 100), (50, 30), 7)
    pygame.draw.line(window, (255, 0, 0), (50, 30), (50, 264), 7)
    pygame.draw.line(window, (255, 0, 0), (50, 264), (100, 100), 7)
    # Lines (multiple)
    pygame.draw.lines(window, (0, 0, 255), True, ((50, 30), (75, 75), (128, 64), (97, 57), (200, 29)), 5)


    pygame.display.update()