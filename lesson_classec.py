# class Human:
#     def __init__(self, age, heigth, eye_color):
#         self.age = age
#         self.heigth = heigth
#         self.eye_color = eye_color
#         print('hallo')

#     def say_hello(self):
#         print(f'HI. im {self.age}')


# Max = Human(18, 125, 'Blue')

# print(f'im {Max.eye_color}')

# Dima = Human(16, 188, 'Green')
# print(f'im {Dima.age}')
# Dima.age = 16
# print(f'im {Dima.age}')
# Dima.say_hello()

import pygame
import random
from my_cricle import My_Circle 

pygame.init()

W, H = 500, 500
SIZE = (W, H)
sc = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()
change = 1

# class My_Circle():

#     def __init__(self, x, y, rad, direkt, color=(0, 0, 0)):
#         self.x, self.y = x, y
#         self.color = color
#         self.rad = rad
#         self.direkt = direkt
    
#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color,\
#                 (self.x, self.y), self.rad)
        
    
#     def move(self, screen):
#         global change
#         keys = pygame.key.get_pressed()

#         if keys[pygame.K_w]:
#             self.y -= 1
#         if keys[pygame.K_s]:
#             self.y += 1
#         if keys[pygame.K_a]:
#             self.x -= 1
#         if keys[pygame.K_d]:
#             self.x += 1
#         if keys[pygame.K_ESCAPE]:
#             pygame.quit()
#         if keys[pygame.K_c]:
#             sc.fill((0, 0, 0)) 
#         if change == 1:
#             if keys[pygame.K_SPACE]:
#                 self.color = (255, 0 ,0)
#                 change = -1
#                 pygame.time.delay(100)
#         elif change == -1:
#             if keys[pygame.K_SPACE]:
#                 self.color = (30, 150, 100)
#                 change = 1
#                 pygame.time.delay(100)
#     def move_hor(self):
#         if self.direkt == 'right':
#             self.x += 1
#             if self.x > W:
#                 self.direkt = 'left'
#         else:
#             self.x -= 1
#             if self.x < 0:
#                 self.direkt = 'right'

        
        
running = True

circle_1 = My_Circle(W // 2, H // 2, 25, (30, 150, 100))

list_of_circles = []

for i in range(100):
    list_of_circles.append(My_Circle(i * 10, i * 5, i + 10,\
            'rigth' ,random.choices( range(0, 256), k=3)))

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

    circle_1.draw(sc)
    circle_1.move(sc, change)
    sc.fill((0, 0, 0))
    for j in list_of_circles:
        j.draw(sc)
        j.move_hor(W)
        

    
    fps.tick(60)
    pygame.display.update()