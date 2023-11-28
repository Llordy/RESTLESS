# import and initialise libraries
import pygame, sys
from player import Character

pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# GUI configuration
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RESTLESS")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# background of game
background_image = pygame.image.load("attributes/background/background.jpg").convert_alpha()


# scale background to match resolution
def draw_background():
    scaled_background = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))


# Initiate new character
character1 = Character(200, 310)

# main game loop
run = True
while run:

    # clock speed
    clock.tick(FPS)

    # draw background
    draw_background()

    # move character
    character1.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    # draw character
    character1.draw(screen)

    # exit loop if X button is pressed
    # using event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                character1.WKeypressed = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                character1.WKeypressed = False

    # update display
    pygame.display.update()

pygame.quit()