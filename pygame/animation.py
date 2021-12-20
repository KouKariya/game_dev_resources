import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

SIZE = WIDTH, HEIGHT = 150, 150
BACKGROUND_COLOR = pygame.Color('white')
FPS = 5

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('assets/images/blob_0.png'))
        self.images.append(pygame.image.load('assets/images/blob_1.png'))

        #index value to get the image from the array
        #initally it is 0
        self.index = 0

        #now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of the sprite
        self.rect = pygame.Rect(45,45,150,198)

    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index 0 again
            self.index = 0

        #finally we will update the image that will be displayed
        self.image = self.images[self.index]

def quitGame():
    pygame.quit()
    sys.exit()

def main():
    #initializing pygame
    pygame.init()

    #getting the scree of the dpecified size
    screen = pygame.display.set_mode(SIZE)

    #creating our sprite object
    my_sprite = MySprite()

    #creating a group with our sprite
    my_group = pygame.sprite.Group(my_sprite)

    #getting the pygame clock for handling fps
    clock = pygame.time.Clock()

    while True:
        # updating the sprite()
        my_group.update()

        # filling the screen with background color
        screen.fill(BACKGROUND_COLOR)

        # drawing th sprite
        my_group.draw(screen)

        # updating the display
        pygame.display.update()
        #if the event is quit means we clicked on the close window button
        for event in GAME_EVENTS.get():
            if event.type == GAME_GLOBALS.QUIT:
                quitGame()



        #ginally delaying the loop with clock tick for 10fps
        clock.tick(FPS)

main()