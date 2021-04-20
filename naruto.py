import pygame
dir = -1
class Naruto:
    def __init__(self, x, y, h, w, img):
        self.x, self.y, self.h, self.w = x, y ,h ,w
        self.img = img 
    

    def draw_nar(self,sc):
        if dir == -1:
            sc.blit(self.img, (self.x ,self.y))
        else:
            sc.blit(pygame.transform.flip(self.img, True, False), (self.x, self.y))

    def move_naruto(self):
        global dir
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 2
            dir = -1
        if keys[pygame.K_RIGHT]:
            self.x += 2
            dir = 1  
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2
        if self.x > self.w - 100:
            self.x = 100
        if self.x < 100:
            self.x = self.w - 100
        if self.y > self.h:
            self.y = 0 
        if self.y < 0:
            self.y = self.h
        if keys[pygame.K_ESCAPE]:
            exit()
