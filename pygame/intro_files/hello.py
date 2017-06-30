import pygame

#gets ready to use pygame module
pygame.init()

#sets the display window for the game (width,height)
window = pygame.display.set_mode((500, 400))

while True:
	#What to draw - #surface - #color - #X-coor,Y-coor,width,height
	#pygame.draw.rect(window, (255,0,0),(100,100,50,50))
	#pygame.draw.rect(window, (0,255,0),(150,100,50,50))
	#pygame.draw.rect(window, (0,0,255),(200,100,50,50))

	#draw a circle	#surface - #color - #X,Ycoor - #radius #width of circ line	
	pygame.draw.circle(window, (255,255,0),(200,200), 20, 0)
	pygame.draw.circle(window, (225,225,0),(300,200), 20, 2)

	#Draws a full ellipse within a hollow rectangle
	#draw an ellipse - #color - #X,Ycoor - width - height
	pygame.draw.rect(window, (255,0,0),(100,100,100,50),2)
	pygame.draw.ellipse(window, (255,0,0),(100,100,100,50))

	pygame.display.update()
