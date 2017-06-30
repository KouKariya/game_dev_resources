###TOP###
import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame Shapes!")

###CHUNK 01###   Sporatically moves a red square randomly
#while True:
#	#Clears pixel data from prev frame.
#	surface.fill((0,0,0))
#	pygame.draw.rect(surface,(255,0,0), (random.randint(0,windowWidth),random.randint(0,windowHeight), 10, 10))

###CHUNK 02###   Moves a green square either horiz/vert/or diagonally
#greenSquareX = windowWidth / 2
#greenSquareY = windowHeight / 2

#while True:
#	surface.fill((0,0,0))
#	pygame.draw.rect(surface, (0,255,0), (greenSquareX, greenSquareY, 10, 10))
#	#greenSquareX += 1
#	greenSquareY += 1
	
###CHUNK 03###   Moves a blue square diagonally but accelerates its speed
#blueSquareX = 0.0
#blueSquareY = 0.0
#blueSquareVX = 1
#blueSquareVY = 1

#while True:
#	surface.fill((0,0,0))
#	pygame.draw.rect(surface,(0,0,255),(blueSquareX,blueSquareY,10,10))
#	blueSquareX += blueSquareVX
#	blueSquareY += blueSquareVY
#	blueSquareVX +=0.1
#	blueSquareVY += 0.1

###CHUNK 04###   Creates a square in the center that expands while staying in place
#rectX = windowWidth / 2
#rectY = windowHeight / 2
#recWidth = 50
#recHeight = 50

##while True:
#	surface.fill((0,0,0))
#	pygame.draw.rect(surface,(255,255,0),(rectX-recWidth /2, rectY-recHeight /2, recWidth, recHeight))
#	recWidth +=1
#	recHeight += 1

###CHUNK 05###  cycles thru the RGB color group, resets to diff color after reaching limit(255)
squaresRed = random.randint(0,255)
squaresBlue = random.randint(0,255)
squaresGreen = random.randint(0,255)

while True:
	surface.fill((0,0,0))
	pygame.draw.rect(surface,(squaresRed, squaresBlue, squaresGreen), (50,50,windowWidth/2,windowHeight/2))
	if squaresRed >= 255:
		squaresRed = random.randint(0,255)
	else:
		squaresRed += 1
	if squaresGreen >= 255:
		squaresGreen = random.randint(0,255)
	else:
		squaresGreen += 1
	if squaresBlue >= 255:
		squaresBlue = random.randint(0,255)
	else:
		squaresBlue += 1

###BOTTOM###
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
