''' shapes.py
# Written by Jesse Gallarzo
# Program that '''

import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:
    #Shows hollow rectangles with ellipses inside of them
    pygame.draw.rect(window, (255, 0, 0), (100, 100, 100, 50), 2)
    pygame.draw.ellipse(window, (255, 0, 0), (100, 100, 100, 50))
    #
    pygame.draw.rect(window, (0, 255, 0), (100, 150, 84, 40), 2)
    pygame.draw.ellipse(window, (0, 255, 0), (100, 150, 80, 40))
    #
    pygame.draw.rect(window, (0, 0, 255), (100, 190, 60, 30), 2)
    pygame.draw.ellipse(window, (0, 0, 255), (100, 190, 60, 30))
    # Circle made with ellipse
    pygame.draw.ellipse(window, (0, 0, 255), (100, 250, 40, 40))

    pygame.display.update()