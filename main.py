import pygame
CLOCK = pygame.time.Clock()

SCREENWIDTH = 860
SCREENHEIGHT = 540

x = pygame.display
x.set_mode((SCREENWIDTH, SCREENHEIGHT))
x.set_caption("Stop spying on me :D")
character1 = pygame.rect.Rect(0,0,10,10)



#main loop
run = True
while run:
    CLOCK.tick(60)
    pygame.draw.rect(x, "red", character1, 100)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
