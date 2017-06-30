import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

#Pygame variables
pygame.init()

windowWidth = 800
windowHeight = 500

surface = pygame.display.set_mode((windowWidth,windowHeight))

pygame.display.set_caption("Window Title!")

def quitGame():
	pygame.quit()
	sys.exit()

while True:
	#Event for closing window
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			quitGame()

	#Refreshes the screen, updates w/ any changes
	pygame.display.update()
