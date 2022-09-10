import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

#Pygame variables
pygame.init()
windowWidth = 800
windowHeight = 500

surface = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("RPG Test!")

#Player variables
playerSize = 20
playerX = (windowWidth / 2) -(playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 1.0
moveSpeed = 1.0

#Keyboard variables
leftDown = False
rightDown = False
upDown = False
downDown = False

#Function that determines how the player moves
def move():
	global playerX, playerY, playerVX, playerVY
	if leftDown:
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX
		#Make sure player doesn't leave window
		if playerX > 0:
			playerX += playerVX
	if rightDown:
		if playerVX < 0.0:
			playerVX = moveSpeed
		#make sure player doesnt leave window
		if playerX + playerSize < windowWidth:
			playerX += playerVX

	if upDown:
		if playerVY > 0.0:
			playerVY = moveSpeed
		#make sure player doesnt leave window
		if playerY > 0.0:
			playerY -= playerVY

	if downDown:
		if playerVY < 0.0:
			playerVY = -moveSpeed
		#make sure player doesn't leave window
		if playerY + playerSize < windowHeight:
			playerY += playerVY
def quitGame():
	pygame.quit()
	sys.exit()

while True:
	surface.fill((0,255,0))

	#Draw our character
	pygame.draw.rect(surface,(255,0,0), (playerX,playerY,playerSize,playerSize))

	#Looks for different events
	for event in GAME_EVENTS.get():
		
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				upDown = True
			if event.key == pygame.K_DOWN:
				downDown = True
			if event.key == pygame.K_ESCAPE:
				quitGame()
		
		if event.type == pygame.KEYUP:
			
			if event.key  == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed #LOOKUP
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_UP:
				upDown = False
				playerVY = moveSpeed
			if event.key == pygame.K_DOWN:
				downDown = False
				playerVY = moveSpeed

		#Event for closing window
		if event.type == GAME_GLOBALS.QUIT:
			quitGame()
	move()
	#Refreshes the screen, updates w/ any changes
	pygame.display.update()
