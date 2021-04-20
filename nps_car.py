import pygame


class Nps_car:
    
    def __init__(self, x, y, w, h, img):
        self.x, self.y = x, y        
        self.w, self.h = w, h
        self.img = img
    
    def draw (self,sc):
        sc.blit(self.img, (self.x, self.y))
    
    def move_up(self):
        
        self.y -= 3
       
        if self.y < 0:
            return 1
        else:
            return 0
        
    
    def move_down(self):
        self.y += 3
        if self.y > self.h:
            return 1
        else:
            return 0  