import pygame

pygame.init()

W, H = 500, 500
SIZE = (W, H)

GRAY = [70] * 3
WHITE = [255] * 3
BLACK = [0] * 3

sc = pygame.display.set_mode(SIZE)

img = pygame.image.load('naruto.png')
img_transform = pygame.transform.scale(img, (50, 50))
img_transform_1 = pygame.transform.rotate(img_transform, 90)

running = True

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    sc.blit(img_transform_1, (W // 2, H // 2))
    pygame.display.update()