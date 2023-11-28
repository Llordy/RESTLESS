import pygame
import time

class Character():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 160))
        self.vel_y = 0
        self.hasJumped = False
        self.airTime = 0
        self.temp1 = []
        self.temp2 = []



        self.attack_type = 0

        self.jumpsAvailable = 1

    def move(self, screen_width, screen_height):

        JUMP_SPEED = -30






        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        jumpsMax = 1

        #get the key presses
        key = pygame.key.get_pressed()
        mouse_key = pygame.mouse.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx += -SPEED
        if key[pygame.K_d]:
            dx += SPEED

        #jumping

#this was an attempt that didn't work
        # if key[pygame.K_w] and self.flag:
        #         self.vel_y += JUMP_SPEED
        #         self.djump += self.vel_y
        #         print(self.djump)
        #         if self.djump < JUMP_MAX_DIFFERENCE:
        #             print("Yes")
        #             self.flag = False
        #         print(self.flag)
        # elif self.rect.top == 310:
        #     self.flag = True
        #     self.djump = 0


#this version worked

#        if self.rect.top == 310 and key[pygame.K_w]:
#            self.jump_tick = 1
#
 #       if key[pygame.K_w]:
 #           if self.jump_tick <= JUMP_MAX_TICK and self.rect.top > 150:
 #               self.vel_y += JUMP_SPEED
#
  #      elif self.rect.top == 310:
   #         self.jump_tick = 0


#attempt #3
#        if key[pygame.K_w]:
#            if self.rect.top >= 310 or self.jumpsUsed != jumpsMax:
#                Still_Pressed = True
#                self.jumpsUsed += 1
#                self.vel_y += JUMP_SPEED

        #if

         # if key[pygame.k_w] and (self.airTime < )
         #
        # if self.rect.bottom < 470:
        #     self.airTime += 1
        #     print(self.airTime)
        #     self.temp1.append(self.rect.bottom)
        #
        # else:
        #     if len(self.temp1) > 0:
        #         print((sum(self.temp1)/len(self.temp1)))
        #         print(max(self.temp1))
        #         self.temp1 = []
        #
        #
        #
        #     self.airTime = 0
        #
        #
        #
        # if self.hasJumped == False:
        #     if key[pygame.K_w] and self.vel_y > -30:
        #         self.vel_y += JUMP_SPEED
        #
        #
        #
        # if (self.vel_y < -30 or self.vel_y > 0):
        #         #and self.rect.top < 310
        #     self.hasJumped = True
        #
        #
        #
        #
        if key[pygame.K_w] and self.jumpsAvailable > 0:
            self.vel_y = JUMP_SPEED
            self.jumpsAvailable = 0

        # apply gravity
        if self.vel_y > 30:
            ...
        else:
            self.vel_y += GRAVITY


            dy += self.vel_y








        #keep character out of boundary
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        if self.rect.bottom + dy > 470:
            self.vel_y = 0
            dy = 470 - self.rect.bottom
            if self.rect.bottom == 470:
                self.hasJumped = False



    #attacking
        if mouse_key[0]:
            print("left click pressed")


        #update position of character
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.top == 310:
            self.jumpsAvailable = 1


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
