import pygame

pygame.init()

W, H = 500, 500
SIZE = (W, H)

GRAY = [70] * 3
WHITE = [255] * 3
BLACK = [0] * 3

sc = pygame.display.set_mode(SIZE)

running = True
pygame.mouse.set_visible(False)

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pressed = pygame.mouse.get_pressed()
# [0]- левая кнопака , [1]- правая кнопка , [2]- нажатие на колесо, [3]- колесо вверх, [4]- колесо вниз
    if pressed[0]:
        # координаты курсора через 2 переменные
        # x, y = pygame.mouse.get_pos()
        # координаты курсора через индексацию списка
        # pos = pg.mouse.get_pos()
        # pg.draw.rect(
        #     sc, BLUE, (pos[0] - 10,
        #                pos[1] - 10,
        #                20, 20))
        pygame.draw.circle(sc, WHITE, pygame.mouse.get_pos(), 5)
    pygame.display.update()