''' hello.py
Written by Jesse Gallarzo
An introduction program about the pygame module. '''
import pygame

pygame.init()

# parameter that tells how the window should look
# width first(500) lenght(400)
window = pygame.display.set_mode((500, 400))  # <--Tuple of numbers

while True:
    # creates a rectangle, (255,0,0)= RGB color scheme
    # 2nd set of colors(x coor, y coor, width of rect, height of rect)
    # pygame.draw.rect(window, (255, 0, 0), (100, 100, 50, 50))
    # pygame.draw.rect(window, (0, 255, 0), (150, 100, 50, 50))
    # pygame.draw.rect(window, (0, 0, 255), (200, 100, 50, 50))

    # draw circle, (RBG),(location/point),radius,line-width
    pygame.draw.circle(window, (255, 255, 0), (250, 200), 20, 0)

    pygame.display.update()