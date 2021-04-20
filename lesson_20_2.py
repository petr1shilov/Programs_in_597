import pygame
import random

W, H = 1000, 700

pygame.init()
win = pygame.display.set_mode((W, H))

size = 70
flag = 1

clock = pygame.time.Clock()
FPS = 110
pygame.mouse.set_visible(False)
object_to_draw = 'circle'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        object_to_draw = 'rect'
    elif keys[pygame.K_w]:
        object_to_draw = 'circle'
    elif keys[pygame.K_SPACE]:
        win.fill((0, 0, 0))

    size += flag
    if size > 140:
        flag = -1
    if size < 25:
        flag = 1

    if object_to_draw == 'circle':
        pygame.draw.circle(win, random.choices(range(0, 256), k = 3), pygame.mouse.get_pos(), size // 2)
    elif object_to_draw == 'rect':
        x, y = pygame.mouse.get_pos()
        pygame.draw.rect(win, random.choices(range(0, 256), k = 3), (x - size//2, y-size//2, size, size))

    pygame.display.update()
    clock.tick(FPS)
