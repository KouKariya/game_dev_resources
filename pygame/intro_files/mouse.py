import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

#Pygame variables
pygame.init()

windowWidth = 800
windowHeight = 500

surface = pygame.display.set_mode((windowWidth,windowHeight))

pygame.display.set_caption("Pygame Mouse!")

#Mouse variables
mousePosition = None
mousePressed = False

#Square variables
squareSize = 40
squareColor = (255,0,0)
squareX = windowWidth / 2
squareY = windowHeight - squareSize
draggingSquare = False
gravity = 5.0

def checkBounds():
	global squareColor, squareX, squareY, draggingSquare
	if mousePressed == True:
		#Is our cursor over the square?
		if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:
			if mousePosition[1] > squareY and mousePosition[1] < squareY + squareSize:
				draggingSquare = True
				pygame.mouse.set_visible(0)

	else:
		squareColor = (255,0,0)
		pygame.mouse.set_visible(1)
		draggingSquare = False

def checkGravity():
	global gravity, squareColor, squareY, squareSize, windowHeight
	
	#Is our square in the air and have we let go of it?
	if squareY < windowHeight - squareSize and mousePressed == False:
		squareY += gravity
		gravity = gravity * 1.1
	else:
		squareY = windowHeight - squareSize
		gravity = 5.0
	 
def drawSquare():
	global squareColor, squareX, squareY, draggingSquare
	if draggingSquare == True:
		squareColor = (0,255,0)
		squareX = mousePosition[0] - squareSize/2
		squareY = mousePosition[1] - squareSize/2
	
	pygame.draw.rect(surface,squareColor,(squareX,squareY,squareSize,squareSize))

def quitGame():
	pygame.quit()
	sys.exit()

while True:
	mousePosition = pygame.mouse.get_pos()
	
	surface.fill((0,0,0))

	#Check whether if the mouse is pressed down
	if pygame.mouse.get_pressed()[0] == True:
		mousePressed = True
	else:
		mousePressed = False

	checkBounds()
	checkGravity()
	drawSquare()
 
	pygame.display.update()

	#Event for closing window
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			quitGame()
