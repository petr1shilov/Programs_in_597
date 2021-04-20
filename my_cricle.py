import pygame
import random


class My_Circle():

    def __init__(self, x, y, rad, direkt, color=(0, 0, 0)):
        self.x, self.y = x, y
        self.color = color
        self.rad = rad
        self.direkt = direkt
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color,\
                (self.x, self.y), self.rad)
        
    
    def move(self, screen, change):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= 1
        if keys[pygame.K_s]:
            self.y += 1
        if keys[pygame.K_a]:
            self.x -= 1
        if keys[pygame.K_d]:
            self.x += 1
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if keys[pygame.K_c]:
            screen.fill((0, 0, 0)) 
        if change == 1:
            if keys[pygame.K_SPACE]:
                self.color = (255, 0 ,0)
                change = -1
                pygame.time.delay(100)
        elif change == -1:
            if keys[pygame.K_SPACE]:
                self.color = (30, 150, 100)
                change = 1
                pygame.time.delay(100)
    def move_hor(self, W):
        if self.direkt == 'right':
            self.x += 1
            if self.x > W:
                self.direkt = 'left'
        else:
            self.x -= 1
            if self.x < 0:
                self.direkt = 'right'
