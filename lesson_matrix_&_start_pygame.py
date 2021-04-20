# matrix = [[1, 3, 5], [2 ,4 ,5], [4, 3, 3]]

# print(matrix[2][2], matrix[0][1])

# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j], end='\t')
#     print()


# table = [[input(el)] for el in input().split()]

# d = {'slovar' : 1, \
#         'slovar2' : 2}
# print(d['slovar2'])
# d['slovar2'] = 'pop'
# print(d['slovar'])
# print(d['slovar2'])



# print(d.items())
# print(d.values())
# print(d.keys())
# print(d)

import pygame

color = (255, 255, 255)

pygame.init()

W, H = 500, 500
x, y = W // 2, H // 2
sc = pygame.display.set_mode((W, H))
fps = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # sc.fill((30, 255, 8))
    # x += 1
    # if x > W:
    #     x = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        y += 1
        if y > H:
            y = 0 
    if keys[pygame.K_UP]:
        y -= 1
        if y < 0:
            y = H 
    if keys[pygame.K_LEFT]:
        x -= 1
        if x < 0:
            x = W 
    if keys[pygame.K_RIGHT]:
        x += 1
        if x > W:
            x = 0 
    if keys[pygame.K_ESCAPE]:
        exit()
    

    pygame.draw.circle(sc, (255)*3,(x, y), 25)
    pygame.display.update()
    fps.tick(60)

    # pygame.draw.circle(sc, color,(250, 250), 200, 5)
    # pygame.draw.rect(sc, (13, 126, 188),(250, 250, 100, 50))
    # # pygame.draw.lines(sc, (0, 0, 0), True, ((0, 0), (200,100), (255, 255)), 10)
    # pygame.draw.aaline(sc, (0, 0, 0),(0, 0), (200,100), 30)
    # pygame.draw.polygon(sc, color,[], False)
    # for i in range(10):
    #     pygame.draw.ellipse(sc,(0, 0, 0),\
    #         (i * 15, 0, 500 - i * 30, 500), 1)
    # for j in range(10):
    #     pygame.draw.ellipse(sc,(0, 0, 0),\
    #         (0, j * 15, 500, 500 - j * 30), 1)
    # pygame.display.update()
    