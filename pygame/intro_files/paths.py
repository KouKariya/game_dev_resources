import pygame

pygame.init()
window = pygame.display.set_mode((500,400))

while True:
	#draw a white line                    #where the line starts
	#                                           #where the line ends
	#                                                    #line width
	#pygame.draw.line(window, (255,255,255),(0,0),(500,400),1)


	#pygame.draw.line(window, (255,255,255),(50,50),(75,75), True)
	#pygame.draw.line(window, (255,255,255),(75,75),(25,75), True)
	#pygame.draw.line(window, (255,255,255),(25,75),(50,50), True)

	#pygame.draw.lines(WHERE TO DRAW, COLOR, CLOSE THE SHAPE?, THE POINTS TO DRAW, LINE WIDTH)
	pygame.draw.lines(window,(255,255,255), True, ((50,50),(75,75),(63,100),(38,100),(25,75)),1)

	pygame.display.update()
